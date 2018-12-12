import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# Atrributes of logging - https://docs.python.org/3/library/logging.html#logrecord-attributes

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(name)s:%(message)s:%(levelname)s')
file_handler = logging.FileHandler('/Users/nayak/repositories/python_repository/logging/product_logs.log')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


# logging.basicConfig(filename='/Users/nayak/repositories/python_repository/logging/product_logs.log',
#                     level=logging.INFO,
#                     format='%(name)s:%(message)s:%(levelname)s',
#                     filemode='a')


class ProductInventory:
    bill_amount = 0

    def __init__(self, product_name, items_in_stock, price):
        self.product_name = product_name
        self.items_in_stock = items_in_stock
        self.price = price
        logger.info("Product {} created with Rs. {} per piece. Total {} in inventory is {}"
                    .format(self.product_name, self.price, self.product_name, self.items_in_stock))

    def sell(self, units):
        self.items_in_stock = self.items_in_stock - units
        bill_amount = self.price * units
        logger.info("Revenue from {} {} is: {}".format(units, self.product_name, bill_amount))
        logger.info("Number of {} left in the inventory is: {}".format(self.product_name, self.items_in_stock))

    def add(self, units):
        logger.info("{} units of {} added to inventory".format(units, self.product_name))
        logger.info("Number of {} left in the inventory is: {}".format(self.product_name, self.items_in_stock))


pen = ProductInventory('Pen', 10, 2)
ProductInventory.sell(pen, 5)
ProductInventory.add(pen, 10)
