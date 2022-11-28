from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):  # default parameter
        super().__init__(
            name, price, quantity
        )
        # Run validation to the received arguments
        assert broken_phone >= 0, f"Broken phones {broken_phone} is not greater than or equal to zero!"
        # Assign to self object
        self.broken_phones = broken_phone
