from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# Function to check if AP List is displayed on screen upon entering API KEY
# Args:
#       driver_obj : Appium webdriver object corresponding to the simulator
#       timeout : Time (in seconds) to wait if the elements are displayed or not
#
# Returns:
#       status : If True implies the AP list was populated
#                If False implies the AP list was not populated
def check_if_ap_list_is_displayed(driver_obj, timeout):

    status = True
    wait = WebDriverWait(driver_obj, timeout)
    try:
        wait.until(ec.presence_of_element_located((By.XPATH, "//XCUIElementTypeCell")))
    except:
        status = False

    return status


def click_wireless_button(driver_obj, timeout):

    driver_obj.find_element_by_accessibility_id("Wireless").click()
    page_status = check_if_ap_list_is_displayed(driver_obj, timeout)

    return page_status


# Fetch names of all AP upon successful login
# Args:
#       driver_obj : Appium webdriver object corresponding to the simulator
#
# Returns:
#       ap_list : list with names of the APs available
def fetch_ap_list_details(driver_obj):

    ap_list = []
    ap_names = driver_obj.find_elements_by_xpath("//XCUIElementTypeCell")
    for ap_name in ap_names:
        ap_list.append((ap_name.text))

    return ap_list


# Function to confirm ap page was generated
# Args:
#       driver_obj : Appium webdriver object corresponding to the simulator
#       timeout : Time (in seconds) to wait if the elements are displayed or not
#       ap_name : Name of the AP whose details are displayed
#
# Returns:
#       status: If True implies the AP page was populated
#               If False implies the AP page was not populated
def check_if_ap_page_generated(driver_obj, timeout, ap_name):

    status = True
    wait = WebDriverWait(driver_obj, timeout)
    try:
        wait.until(ec.presence_of_element_located((By.ID, ap_name)))
    except:
        status = False

    return status


# Confirm if details for each AP item are displayed
# Note : This function expects simulator at screen with list of AP
# Args:
#       driver_obj : Appium webdriver object corresponding to the simulator
#       ap_name : Name of the ap_list item to click
#       timeout : to open the new screen displaying details
#
# Returns:
#       page_status : If True implies the AP page was populated
#                     If False implies the AP page was not populated
def confirm_ap_page_is_displayed(driver_obj, ap_name, timeout):

    driver_obj.find_element_by_accessibility_id(ap_name).click()
    page_status = check_if_ap_page_generated(driver_obj, timeout, ap_name)

    return page_status


# Function to try logging into the app
# Args:
#       driver_obj : Appium webdriver object corresponding to the simulator
#       api_key : input to be entered in the field
#       timeout : Time (in seconds) to wait if the elements are displayed or not
#
# Returns:
#       login_status : If True implies the AP list was populated
#                      If False implies the AP list was not populated
def try_login(driver_obj, api_key, timeout):

    driver_obj.close_app()
    driver_obj.launch_app()
    driver_obj.find_element_by_accessibility_id("apiKeyTxt").send_keys(api_key)
    driver_obj.find_element_by_accessibility_id("Go").click()
    # login_status = check_if_ap_list_is_displayed(driver_obj, timeout)
    login_status = confirm_login_success(driver_obj, timeout)

    return login_status


def confirm_login_success(driver_obj, timeout):
    wait = WebDriverWait(driver_obj, timeout)
    page_status = True
    try:
        wait.until(ec.presence_of_element_located((By.NAME, "Maywood Test Network")))
    except:
        page_status = False

    return page_status


# Function to connect to the simulator
# Args:
#       app_config :  python dictionary with all the required details.
#                     Refer config.py for more information
#
# Returns:
#       driver : corresponding webdriver object to interact with the simulator
def connect_to_device(app_config):

    try:
        driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities = app_config
             )
    except:
        emsg = "Could not connect to device - %s. Aborting" %(app_config['deviceName'])
        raise Exception(emsg)

    return driver


# Function to confirm if all elements are populated
# Args:
#        driver_obj : Appium webdriver object corresponding to the simulator
#        ap_name : Name of the ap_list item to click
#        timeout : to open the new screen displaying details
#
# Returns:
#       page_status : If True implies all the AP details were populated
#                     If True implies all the AP details were not populated
def confirm_all_details_displayed(driver_obj, timeout):

    page_status = False
    wait = WebDriverWait(driver_obj, timeout)
    try:
        wait.until(ec.presence_of_element_located((By.ID, "In progress")))
    except:
        page_status = True
    # go back to AP list page
    driver_obj.find_element_by_accessibility_id("Wireless AP's").click()

    return page_status