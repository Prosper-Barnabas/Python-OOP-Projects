from book import *
from user import *

class Admin:
    def __init__(self) -> None:
        self.books = {}
        self.users = {}

    def add_books(self, book_id: int, book_name: str, book_qty: int) -> None:
        pass

    def print_books(self):
        pass

    def search_book(self, book):
        pass

    def borrow_book(self, book, to_who):
        pass

    def return_book(self, book, from_who):
        pass

    def print_borrowed_users(self):
        pass

    def print_users(self):
        pass


jake = Admin()
jake.add_books(1, "House of Gold", 500)
jake.print_books()