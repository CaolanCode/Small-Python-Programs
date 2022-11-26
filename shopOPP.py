class Item:
    def __init__(self, name: str, price: float, quantity=0):  # default parameter
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)
item2.has_numpad = False  # can use attributes that aren't in constructor

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
print("Has number pad: ", item2.has_numpad)
