import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# Atrributes of logging - https://docs.python.org/3/library/logging.html#logrecord-attributes

logging.basicConfig(level=logging.DEBUG)


class ProductInventory:
    bill_amount = 0

    def __init__(self, product_name, items_in_stock, price):
        self.product_name = product_name
        self.items_in_stock = items_in_stock
        self.price = price
        logging.debug("Product {} created with Rs. {} per piece. Total {} in inventory is {}"
                      .format(self.product_name, self.price, self.product_name, self.items_in_stock))

    def sell(self, units):
        self.items_in_stock = self.items_in_stock - units
        bill_amount = self.price * units
        logging.debug("Revenue from {} {} is: {}".format(units, self.product_name, bill_amount))
        logging.debug("Number of {} left in the inventory is: {}".format(self.product_name, self.items_in_stock))

    def add(self, units):
        self.items_in_stock = self.items_in_stock + units
        logging.debug("{} units of {} added to inventory".format(units, self.product_name))
        logging.debug("Number of {} left in the inventory is: {}".format(self.product_name, self.items_in_stock))


pen = ProductInventory('Pen', 10, 2)
ProductInventory.sell(pen, 5)
ProductInventory.add(pen, 10)
