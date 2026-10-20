from book import *
from user import *

class Admin:
    def __init__(self) -> None:
        self.books = {}
        self.users = {}

    def add_books(self, book_id: int, book_name: str, book_qty: int) -> None:
        existing_books = [book.name for book in self.books.values()]
        if book_name in existing_books:
            print(f"{book_name} already exists")
            return
        if book_id in self.books:
            print(f"Book ID: {book_id} already exists")
            return
        new_book = Book(book_id, book_name, book_qty)
        self.books[book_id] = new_book
        print(f"{book_name} added successfully ✅")

    def print_books(self):
        lst_of_books = []
        if not self.books:
            print("There are no books")
            return
        for book in self.books.values():
            lst_of_books.append(book.name)

        print(', '.join(lst_of_books))

    def search_book(self, query):
        pass

    def add_user(self, user_id: int, user_fname: str, user_lname: str):
        user_full_name = user_fname + " " + user_lname
        existing_users = [user.full_name for user in self.users.values()]
        if user_id in self.users:
            print(f"User ID: {user_id} already exists")
            return
        if user_full_name in existing_users:
            print(f"{user_full_name} already exists")
            return
        new_user = User(user_id, user_fname, user_lname)
        self.users[user_id] = new_user
        print(f"{user_full_name} added successfully ✅")

    def borrow_book(self, book_name, user_name):
        pass

    def return_book(self, book_name, user_name):
        pass

    def print_borrowed_users(self):
        pass

    def print_users(self):
        lst_of_users = []
        if not self.users:
            print("There is no User")
            return
        for user in self.users.values():
            lst_of_users.append(user.name)

        print(lst_of_users)


jake = Admin()
jake.add_books(1, "Yellow Stone", 20)
jake.add_books(2, "Yellow Stone", 20)

jake.print_books()


jake.add_user(1, "Prosper", "Barnabas")
jake.add_user(2, "Prosper", "Barnabas")