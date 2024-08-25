# main.py

from product import Book, Electronic, Clothing

def main():
    # Create instances of each subclass
    my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
    my_electronic = Electronic("456", "Smartphone", 599.99, "64GB, 6GB RAM")
    my_clothing = Clothing("789", "T-Shirt", 19.99, "L")

    # Display information for each product
    print("Book Information:")
    my_book.display_info()
    print("\nElectronic Information:")
    my_electronic.display_info()
    print("\nClothing Information:")
    my_clothing.display_info()

if __name__ == "__main__":
    main()
