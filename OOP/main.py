from Item import Item
from Shopping_Basket import ShoppingBasket

tomatoSoup = Item("Tomato Soup","200mL can", 0.70,20)
spaghetti = Item("Spaghetti","500g pack", 1.10,30)
blackOlives = Item("Black Olives Jar","200g Jar", 2.10,40)
mozarella = Item("Mozarella","100g", 1.50,50)
gratedCheese = Item("Grated Cheese","100g",2.20,60)

myBasket = ShoppingBasket()

myBasket.addItem(tomatoSoup, 4)
myBasket.addItem(blackOlives, 1)
myBasket.addItem(mozarella, 2)
myBasket.addItem(tomatoSoup, 6)

myBasket.view()