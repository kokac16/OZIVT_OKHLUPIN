class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"

class FantasyBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def get_genre(self):
        return f"Genre: {self.genre}"

fantasy_book1 = FantasyBook("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, "Fantasy")

print(fantasy_book1.get_info())
print(fantasy_book1.get_genre())
