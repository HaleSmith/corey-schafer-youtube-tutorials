# References https://www.youtube.com/watch?v=-ARI4Cz-awo
# From https://github.com/CoreyMSchafer/code_snippets/blob/master/Logging-Basics/log-sample.py
# References https://docs.python.org/3/library/logging.html#logrecord-attributes
# References https://www.youtube.com/watch?v=jxmzY9soFXg
import logging
import employee # By importing Employee, code is run

# DEBUG: Detailed information, typically of interest only when
# diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or
# indicative of some problem in the near future (e.g. ‘disk space
# low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able
# to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be
# unable to continue running.

# By default, log will only log warning, error, and critical to console
# By putting in below line, a .log file gets used
# Use pydocs (link above) for format codes
# Note this module gets the ROOT name, and employee gets employee
# logging.basicConfig(filename='sample.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(name)s:%(message)s')

# To make a separate logger for this file:
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)
# This supersedes logger.setLevel
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

# Stream handler to print debug to console
stream_handler = logging.StreamHandler() # Logger already level DEBUG
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result =  x / y
    except ZeroDivisionError:
        # Shows exception in logger
        logger.exception("Tried to divide by zero")
    else:
        return result
num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.critical('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.warning('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

print("See test.log")