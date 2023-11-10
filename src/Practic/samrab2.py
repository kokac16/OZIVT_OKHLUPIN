class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"

    def set_year(self, new_year):
        self.year = new_year

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)

print(book1.get_info())

book1.set_year(1998)

print(book1.get_info())
