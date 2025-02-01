class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)
        print(f"Price after {discount_percentage}% discount: {self.price}")


# Your code for creating a book
book1 = Book("Jamila", "Ch.A", 500)
print(book1.title)
print(book1.author)
print(book1.price)

# Now add the display_info() method
book1.display_info()

# Apply discount
discount = float(input("Enter discount percentage: "))
book1.apply_discount(discount)

