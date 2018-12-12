import logging
import logging_examples

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s|%(name)s:%(message)s:%(levelname)s')
file_handler = logging.FileHandler('/Users/nayak/repositories/python_repository/logging/sample.log')

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


# logging.basicConfig(filename='/Users/nayak/repositories/python_repository/logging/sample.log',
#                     level=logging.DEBUG,
#                     format='%(name)s:%(message)s:%(levelname)s:%(asctime)s',
#                     filemode='a')


def add_num(a, b):
    return a + b


def mul_num(a, b):
    return a * b


def div_num(a, b):
    try:
        result = a / b
    except:
        logger.error("Divison by zero")
        logger.exception("Divison by zero")
    else:
        return result


x = 10
y = 0

sum_value = add_num(x, y)
product_value = mul_num(x, y)
quo_value = div_num(x, y)
logger.debug("Value of {} + {} = {}".format(x, y, sum_value))
logger.debug("Value of {} * {} = {}".format(x, y, product_value))
logger.debug("Value of {} / {} = {}".format(x, y, quo_value))
