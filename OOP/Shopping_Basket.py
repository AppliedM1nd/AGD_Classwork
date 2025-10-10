from item import Item


class ShoppingBasket:
    # Constructor
    def __init__(self):
        self.items = {}  # A dictionary of all the items in the shopping basket: {item:quantity}
        self.checkout = False

    # A method to add an item to the shopping basket
    def addItem(self, item, quantity=1):
        if quantity <= 0:
            print("Invalid operation - Quantity must be a positive number!")
            return None
        if item.stock_level < quantity:
            print(f'There is not enough of {item.name} as there are only {item.stock_level} in stock')
            return None

        item.stock_level -= quantity

        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f'{item.name} x {quantity} added to basket - {item.stock_level} left in stock')

    # A method to remove an item from the shopping basket (or reduce it's quantity)
    def removeItem(self, item, quantity=0):
        if item not in self.items:
            print(f'{item.name} is not currently in the shopping basket')
            return None
        if quantity > self.items[item] or quantity <= 0:
            item.stock_level += self.items[item]
            print(f'The {item.name} has been removed from your basket and the stock of it is now {item.stock_level}')
            self.items.pop(item, None)

        else:
            self.items[item] -= quantity
            item.stock_level += quantity
            print(
                f'{quantity} of {item.name} has been removed so there are now {self.items[item]} in your basket and {item.stock_level} in stock')

    # A method to update the quantity of an item from the shopping basket
    def updateItem(self, item, quantity):
        if item not in self.items:
            print(f'{item.name} is not currently inside the basket')
            return None
        if quantity <= 0:
            self.removeItem(item)
            return None
        current = self.items[item]
        if quantity > current:
            diff = quantity - current
            if diff > item.stock_level:
                print('Not enough stock available')
                return None
            else:
                item.stock_level -= diff
                self.items[item] = quantity
        else:
            diff = current - quantity
            item.stock_level += diff
            self.items[item] = quantity
        print(f'You now have {quantity} of {item.name} in your basket and there is {item.stock_level} in stock')

    # A method to view/list the content of the basket.
    def view(self):
        totalCost = 0
        print("---------------------")
        for item in self.items:
            quantity = self.items[item]
            cost = quantity * item.price
            print(" + " + item.name + " - " + str(quantity) + " x £" + '{0:.2f}'.format(
                item.price) + " = £" + '{0:.2f}'.format(cost))
            totalCost += cost
        print("---------------------")
        print(" = £" + '{0:.2f}'.format(totalCost))
        print("---------------------")

        # A method to calculate the total cost of the basket.

    def getTotalCost(self):
        totalCost = 0
        for item in self.items:
            quantity = self.items[item]
            cost = quantity * item.price
            totalCost += cost
        return totalCost

    # A method to empty the content of the basket
    def reset(self):
        for item, quantity in self.items.items():
            item.stock_level += quantity
            print(f'Stock of {item.name} is now {item.stock_level}')
        self.items.clear()
        print('The basket has now been emptied')

    # A method to return whether the basket is empty or not:
    def isEmpty(self):
        return len(self.items) == 0

