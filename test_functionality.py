import unittest
import config
import common_functionality
import logger_api

class APList(unittest.TestCase):
    def setUp(self):
        self.driver = common_functionality.connect_to_device(config.app_config)

    def test_ap_list_functionality(self):
        platform_ver = config.app_config["platformVersion"]
        platform_device = config.app_config["deviceName"]
        # opening file with different inputs to test the login functionality
        with open("functional_tp_input.txt", "r") as input_file_obj:

            filename_substr = "functional"

            # creating logger objects
            # 1. will record server logs as well as test output statements
            logger = logger_api.get_logger(filename_substr)
            # 2. will record only test output statements
            msg = "Starting %s Test for %s with %s" % (
            filename_substr, platform_device, platform_ver)
            time_stamp_str = logger_api.get_timestamp_str()
            test_log_file_name = "test_log_%s_%s.txt" % (filename_substr, time_stamp_str)
            logger_api.vmTrace(test_log_file_name, msg)

            for input in input_file_obj:
                # try logging into app using the API KEY mentioned in sanity_tp_input.txt file
                login_status = common_functionality.try_login(self.driver, input,
                                                              config.populate_api_list_timeout)

                if not login_status:
                    output_string = "could not login. Skipping to next run"
                    # write test result to logger
                    logger_api.log_details(logger, test_log_file_name, output_string)
                    continue

                # click on the Wireless Button to generate the next screen
                page_status = common_functionality.click_wireless_button(self.driver,
                                                                   config.populate_api_list_timeout)

                if not login_status:
                    output_string = "could not login. Skipping to next run"
                    # write test result to logger
                    logger_api.log_details(logger, test_log_file_name, output_string)
                    continue

                # upon successful login get the ap list names
                ap_list = common_functionality.fetch_ap_list_details(self.driver)
                for index, ap_name in enumerate(ap_list):
                    output_string = "platformVersion-%s; device-%s; ListIndex-%s; Result-%s" \
                            %(platform_ver, platform_device, index, ap_name)
                    # write test result to logger
                    logger_api.log_details(logger, test_log_file_name, output_string)

                    # updating the ap_name to match the accessibility ID for the page
                    ap_name = ap_name.split("-")[1].strip()
                    page_status = common_functionality.confirm_ap_page_is_displayed(self.driver,
                                                ap_name, config.ap_page_load_timeout)

                    output_string = "Page Status for %s is %s" %(ap_name, page_status)
                    # write test result to logger
                    logger_api.log_details(logger, test_log_file_name, output_string)

                    all_details_displayed = common_functionality.confirm_all_details_displayed(
                                            self.driver, config.details_per_ap_displayed_timeout)

                    output_string = "All elements for %s page displayed - %s" % (ap_name,
                                                                str(all_details_displayed))

                    # write test result to logger
                    logger_api.log_details(logger, test_log_file_name, output_string)

                # hit back button from AP list to make sure we;re back on landing page

        self.driver.close_app()
        # closing logger handles
        logger_handles = list(logger.handlers)
        for handle in logger_handles:
            logger.removeHandler(handle)
            handle.flush()
            handle.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    unittest.main()