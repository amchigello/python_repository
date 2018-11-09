class inventory:

    # Class Variables
    numberOfProducts = 0
    discountPercentile = 25.0

    # Initialize an object of the class
    def __init__(self, product_name, items_in_stock, price):
        self.product_name = product_name
        self.items_in_stock = items_in_stock
        self.price = price
        inventory.numberOfProducts += 1

    #Modify the the objects
    def _sell(self, units):
        self.items_in_stock = self.items_in_stock - units
        print("Total Cost for " + str(units) + " " + self.product_name + "(s) : " + str(self.price * units))
        print("Total " + self.product_name + "(s) left in the inventory : " + str(self.items_in_stock))

    #Modify the the objects
    def _add(self, units):
        self.items_in_stock = self.items_in_stock + units
        print(str(units) + " " + self.product_name + "(s) added to the inventory")
        print("Total " + self.product_name + "(s) left in the inventory : " + str(self.items_in_stock))

    #Demonstrate class variable
    #If self.discountPercentile is not reset inside the method it take the value of inventory.discountPercentile
    def _discount(self, units, discountPercentile):
        oldPrice = self.price
        if discountPercentile is not None:
            self.discountPercentile = discountPercentile
        self.items_in_stock = self.items_in_stock - units
        print("Actual Price of " + self.product_name + ": " + str(self.price))
        self.price = self.price - (self.price * (self.discountPercentile / 100))
        print("Discounted Price of " + self.product_name + ": " + str(self.price))
        print("Total Cost for " + str(units) + " " + self.product_name + "(s) : " + str(self.price * units))
        print("Total " + self.product_name + "(s) left in the inventory : " + str(self.items_in_stock))
        self.price = oldPrice
        self.discountPercentile = inventory.discountPercentile


if __name__ == '__main__':
    penObject = inventory('Pen', 10, 10)
    pencilObject = inventory('Pencil', 25, 2)
    eraserObject = inventory('Eraser', 15, 5)
    rulerObject = inventory('Ruler', 50, 20)
    print("Total number of products: " + str(inventory.numberOfProducts))

    inventory._sell(penObject, 2)
    inventory._sell(pencilObject, 10)
    inventory._sell(eraserObject, 10)

    inventory._add(penObject, 5)
    inventory._add(pencilObject, 5)
    inventory._add(eraserObject, 5)
    inventory._add(rulerObject, 50)

    inventory._discount(rulerObject, 10, 5.0)
    inventory._discount(rulerObject, 10, None)
