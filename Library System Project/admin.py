from book import *
from user import *


class Admin:
    def __init__(self) -> None:
        self.books = {}
        self.users = {}
        self.borrowed_books = {}

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
            lst_of_books.append((book.name, book.id, book.quantity))
            return "\n".join(
                f"Name: {book[0]}, ID: {book[1]}, Quantity: {book[2]}"
                for book in lst_of_books
            )

    def search_book(self, query: int | str):  # searches using ID and book name
        if isinstance(query, int):
            found_books = [
                book.name for book in self.books.values() if query == book.id
            ]
            if not found_books:
                print("No book matched your search.")
                return
        elif isinstance(query, str):
            found_books = [
                book.name
                for book in self.books.values()
                if query.lower() in book.name.lower()
            ]
            if not found_books:
                print("No book matched your search.")
                return

        return "\n".join(found_books)

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

    def search_user(self, query: int | str):
        if isinstance(query, int):
            found_users = [
                user.full_name for user in self.users.values() if query == user.id
            ]
            if not found_users:
                print("No user matched your search.")
                return
        elif isinstance(query, str):
            found_users = [
                user.full_name
                for user in self.users.values()
                if query.lower() in user.full_name.lower()
            ]
            if not found_users:
                print("No user matched your search.")
                return

        return "\n".join(found_users)

    def borrow_book(self, book_name: str, user_name: str) -> None:
        book = None
        for current_book in self.books.values():
            if current_book.name.lower() == book_name.lower():
                book = current_book
                break

        if book is None or book.quantity <= 0:
            print(f"Book: {book_name.title()} is not available")
            return

        user = None
        for current_user in self.users.values():
            if current_user.full_name.lower() == user_name.lower():
                user = current_user
                break

        if user is None:
            print(f"User: {user_name.title()} is not found")
            return

        if user.id not in self.borrowed_books:
            self.borrowed_books[user.id] = []

        self.borrowed_books[user.id].append(book.id)
        book.quantity -= 1
        print(f"{user.full_name.title()} borrowed {book.name.title()}")



    def return_book(self, book_name, user_name):
        pass

    def print_borrowed_users(self):
        pass

    def print_users(self):
        lst_of_users = []
        if not self.users:
            print("There are no Users")
            return
        for user in self.users.values():
            lst_of_users.append(user.name)

        print("\n".join(lst_of_users))


jake = Admin()

jake.add_books(1, "Yellow Stone", 20)
jake.add_books(2, "Yellow Gold", 80)
jake.add_books(3, "Diary of a CEO", 100)
jake.add_books(4, "Rich dad, poor dad", 2000)
jake.add_books(5, "Eat that Frog", 50)

# jake.print_books()

jake.add_user(1, "Tim", "Cook")
jake.add_user(2, "Joel", "Tim")
jake.add_user(3, "Jordan", "Miles")

# jake.print_users()

jake.search_book("yellow")
jake.search_book(3)

jake.search_user(2)
jake.search_user("tim")

print()
jake.borrow_book("eat that frog", "tim cook")
jake.borrow_book("yellow stone", "tim cook")
jake.borrow_book("eat that frog", "jordan miles")