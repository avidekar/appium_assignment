import logging
import datetime
import os


# Function to create the logger object
# Args :
#       tp_name_str : test Plan String name i.e sanity, functional
#
# Returns:
#       logger : logger object to log output
def get_logger(tp_name_str):

    timestamp_str = get_timestamp_str()
    # create filename with current timestamp
    file_name = "serverlogs_%s_%s.txt" % (tp_name_str, timestamp_str)
    # define logger configuration
    logging.basicConfig(filename=file_name,
                        format='%(asctime)s: %(levelname)s: %(message)s ',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG)  # add level to print debug and info messages to
                        # log file

    logger = logging.getLogger()

    return logger


# Function to write test logs specific to unit test to a text file
# Args:
#       file_name : name of the file
#       msg : Output to be written in the file
#
# Returns:
#       Returns nothing
def vmTrace(file_name, msg):

    if os.path.exists(file_name):
        append_write = "a"
    else:
        append_write = "w"

    test_logger = open(file_name, append_write)
    timestamp_str = get_timestamp_str()
    test_line = "[%s] %s \r\n" %(timestamp_str, msg)
    test_logger.write(test_line)
    test_logger.close()


# Function that returns current time in string format
# Args:
#       No arguments needed
#
# Returns:
#       timestamp_str : current time stamp in str. E.g - 2020_Apr_23_21_43_42
def get_timestamp_str():

    datetime_obj = datetime.datetime.now()
    timestamp_str = datetime_obj.strftime("%Y_%b_%d_%H_%M_%S")

    return timestamp_str


# Wrapper function to write output to logs
# Args:
#       logger_obj : logger object that records server logs as well output logs
#       test_log_file_name : file_name that only logs unit test ouptut
#       output_string : print statement
#
# Returns:
#       returns nothing
def log_details(logger_obj, test_log_file_name, output_string):
    logger_obj.info(output_string)
    vmTrace(test_log_file_name, output_string)