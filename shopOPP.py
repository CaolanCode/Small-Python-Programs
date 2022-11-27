import csv


class Item:
    pay_rate = 0.8  # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):  # default parameter
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.quantity}')"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):  # count out the floats that are .0
            return num.is_integer()  # checks if float is .0
        elif isinstance(num, int):
            return True
        else:
            return False


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):  # default parameter
        super().__init__(
            name, price, quantity
        )
        # Run validation to the received arguments
        assert broken_phone >= 0, f"Broken phones {broken_phone} is not greater than or equal to zero!"
        # Assign to self object
        self.broken_phones = broken_phone


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5)

print(Item.all)
print(Phone.all)
