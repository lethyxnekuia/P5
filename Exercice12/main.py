class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title: str = title
        self.author: str = author
        self.year: int = year


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.borrowed_book: list[Book] = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Le livre '{book_title}' a été supprimé")
                return
        raise ValueError(f"Le livre '{book_title}' n'est pas dans la bibliothèque")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_book.append(book)
                print(f"Le livre '{book_title}' a été emprunté")
        raise ValueError(f"Le livre '{book_title}' n'est pas dans la bibliothèque")

    def return_book(self, book_title):
        for book in self.borrowed_book:
            if book.title == book_title:
                self.borrowed_book.remove(book)
                self.books.append(book)
                print(f"Le livre '{book_title}' a été ramené")
        raise ValueError(f"Le livre '{book_title}' n'est pas dans la liste des livres empruntés")

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books(self):
        return [book.title for book in self.borrowed_book]
