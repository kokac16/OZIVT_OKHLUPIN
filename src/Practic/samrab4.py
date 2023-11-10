class Book:
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year

    def get_info(self):
        return f"Title: {self._title}\nAuthor: {self._author}\nYear: {self._year}"

class FantasyBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self._genre = genre

    def get_genre(self):
        return f"Genre: {self._genre}"

fantasy_book1 = FantasyBook("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, "Fantasy")

print(fantasy_book1._title)  
print(fantasy_book1._genre) 

fantasy_book1._title = "New Title"
fantasy_book1._genre = "New Genre"

print(fantasy_book1.get_info())  
print(fantasy_book1.get_genre())  
