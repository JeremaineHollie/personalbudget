class Product:
    def __init__(self, product_id, name, price):
        """Initialize common attributes for all products."""
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        """Display general information about the product."""
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

class Book(Product):
    def __init__(self, product_id, name, price, author):
        """Initialize attributes specific to books."""
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        """Display information about the book, including specific attributes."""
        super().display_info()  # Call the base class method
        print(f"Author: {self.author}")

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        """Initialize attributes specific to electronics."""
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        """Display information about the electronic item, including specific attributes."""
        super().display_info()  # Call the base class method
        print(f"Specifications: {self.specs}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        """Initialize attributes specific to clothing."""
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        """Display information about the clothing item, including specific attributes."""
        super().display_info()  # Call the base class method
        print(f"Size: {self.size}")
