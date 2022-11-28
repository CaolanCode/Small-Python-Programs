from item import Item
from phone import Phone

item1 = Item("MyItem", 250)

item1.__name = "Othername"

print(item1.__name)
