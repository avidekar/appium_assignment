import unittest
import config
import common_functionality
import logger_api


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = common_functionality.connect_to_device(config.app_config)

    def test_login(self):
        platform_ver = config.app_config["platformVersion"]
        platform_device = config.app_config["deviceName"]
        # opening file with different inputs to test the login functionality
        with open("sanity_tp_input.txt", "r") as input_file_obj:
            filename_substr = "sanity"

            # creating logger objects
            # 1. will record server logs as well as test output statements
            logger = logger_api.get_logger(filename_substr)
            # 2. will record only test output statements
            msg = "Starting %s Test for %s with %s" %(filename_substr, platform_device, platform_ver)
            time_stamp_str = logger_api.get_timestamp_str()
            test_log_file_name = "test_log_%s_%s.txt" %(filename_substr, time_stamp_str)
            logger_api.vmTrace(test_log_file_name, msg)

            for input in input_file_obj:
                # try logging into app using the API KEY mentioned in sanity_tp_input.txt file
                login_status = common_functionality.try_login(self.driver, input,
                                                              config.populate_api_list_timeout)

                output_string = "platformVersion-%s; device-%s; Input-%s; Result-%s" \
                            %(platform_ver, platform_device, input, str(login_status))

                # write test result to logger
                logger_api.log_details(logger, test_log_file_name, output_string)

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
