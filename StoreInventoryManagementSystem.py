class Product:

    total_products = 0

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        Product.total_products += 1

    def sell(self, quantity):
        if quantity <= 0 :
            return "Invalid quantity"
        elif quantity > self.stock:
            return "Not enough stock"
        else:
            self.stock -= quantity
            return f"number of product in now: {self.stock}"

    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True
        else:
            return False

    @classmethod
    def get_total_products(cls):
        return cls.total_products