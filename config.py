import os

app_path = os.path.join(os.getcwd(), "Meraki_Api_Demo.app")
# simulator configurations
app_config = {
    "app": app_path,
    "platformName": "iOS",
    "platformVersion": "13.0",
    "deviceName": "iPhone 11"
}

# timeout for ap list to populate upon successful API KEY
populate_api_list_timeout = 5

# timeout for per ap page to load
ap_page_load_timeout = 5

# timeout for speecific records to be updated in ap page
details_per_ap_displayed_timeout = 5

