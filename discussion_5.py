import unittest
# what do
# Counts the number of a's in a sentence (e.g., a string)


def count_a(sentence):
    total = 0
    for i in range(len(sentence)):
        if sentence[i] == 'a':
            total += 1
    return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
    # Constructor.
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # Print
    def __str__(self):
        return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.


class Warehouse:

    # Constructor
    def __init__(self, items=[]):
        self.items = items[:]

    # Prints all the items in the warehouse, one on each line.
    def print_items(self):
        for item in self.items:
            print(item)
            print("\n")

    # Adds an item to the warehouse
    def add_item(self, item):
        self.items.append(item)

    # Returns the item in the warehouse with the most stock
    def get_max_stock(self):
        max_stock = 0
        max_name = None
        for item in self.items:
            if item.stock > max_stock:
                max_stock = item.stock
                max_name = item
        return max_name

    # Returns the item in the warehouse with the highest price
    def get_max_price(self):
        max_price = 0
        max_name = None
        for item in self.items:
            if item.price > max_price:
                max_price = item.price
                max_name = item
        return max_name


# Tests
class TestAllMethods(unittest.TestCase):

    # SetUp -- we create a bunch of items for you to use in your tests.
    def setUp(self):
        self.item1 = Item("Beer", 6, 20)
        self.item2 = Item("Cider", 5, 25)
        self.item3 = Item("Water", 1, 100)
        self.item4 = Item("Fanta", 2, 60)
        self.item5 = Item("CocaCola", 3, 40)
        self.item6 = Item("Pepsi", 3, 40)

    # Check to see whether count_a works
    def test_count_a(self):
        aaa_count = count_a("This is aaa sentence.")
        self.assertEqual(aaa_count, 3)
        self.assertEqual(count_a("abcde"), 1)

    # Check to see whether you can add an item to the warehouse

    def test_add_item(self):
        Costco = Warehouse([self.item1, self.item2])
        Costco.add_item(self.item3)
        self.assertEqual(Costco.items, [self.item1, self.item2, self.item3])

    # Check to see whether warehouse correctly returns the item with the most stock

    def test_warehouse_max_stocks(self):
        Costco = Warehouse([self.item1, self.item2, self.item4])
        max_stock = Costco.get_max_stock()
        self.assertEqual(max_stock, self.item4)

        Costco.add_item(self.item3)
        new_max_stock = Costco.get_max_stock()
        self.assertEqual(new_max_stock, self.item3)

    # Check to see whether the warehouse correctly return the item with the highest price
    def test_warehouse_max_price(self):
        Costco = Warehouse([self.item1, self.item2, self.item3])
        max_price = Costco.get_max_price()
        self.assertEqual(max_price, self.item1)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
