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
            print(f"{book_name.title()} already exists")
            return
        if book_id in self.books:
            print(f"Book ID: {book_id} already exists")
            return
        new_book = Book(book_id, book_name, book_qty)
        self.books[book_id] = new_book
        print(f"{book_name.title()} added successfully ✅")

    def print_books(self) -> None:
        lst_of_books = []
        if not self.books:
            print("There are no books")
            return
        for book in self.books.values():
            lst_of_books.append((book.name.title(), book.id, book.quantity))
        print(
            "\n".join(
                f"Name: {book[0]}, ID: {book[1]}, Quantity: {book[2]}"
                for book in lst_of_books
            )
        )

    def search_book(self, query: int | str) -> str | None:
        if isinstance(query, int):
            found_books = [
                book.name.title() for book in self.books.values() if query == book.id
            ]
            if not found_books:
                print("No book matched your search.")
                return
        elif isinstance(query, str):
            found_books = [
                book.name.title()
                for book in self.books.values()
                if query.lower() in book.name.lower()
            ]
            if not found_books:
                print("No book matched your search.")
                return

        return "\n".join(found_books)

    def add_user(self, user_id: int, user_fname: str, user_lname: str) -> None:
        user_full_name = user_fname + " " + user_lname
        existing_users = [user.full_name.title() for user in self.users.values()]
        if user_id in self.users:
            print(f"User ID: {user_id} already exists")
            return
        if user_full_name in existing_users:
            print(f"{user_full_name.title()} already exists")
            return
        new_user = User(user_id, user_fname, user_lname)
        self.users[user_id] = new_user
        print(f"{user_full_name.title()} added successfully ✅")

    def search_user(self, query: int | str) -> str | None:
        if isinstance(query, int):
            found_users = [
                user.full_name for user in self.users.values() if query == user.id
            ]
            if not found_users:
                print("No user matched your search.")
                return
        elif isinstance(query, str):
            found_users = [
                user.full_name.title()
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

        if book.id in self.borrowed_books[user.id]:
            print(f"{user.full_name.title()} has already borrowed {book.name.title()}")
            return

        self.borrowed_books[user.id].append(book.id)
        book.quantity -= 1
        print(f"{user.full_name} borrowed {book.name}")

    def return_book(self, book_name: str, user_name: str) -> None:
        book = None
        for current_book in self.books.values():
            if current_book.name.lower() == book_name.lower():
                book = current_book
                break

        if (
            book is None
        ):  # why is it that I cannot perform a book.id operation using and it has to be or
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
            print(f"{user.full_name.title()} has not borrowed any book")
            return

        if book.id not in self.borrowed_books[user.id]:
            print(f"{user.full_name.title()} did not borrow {book.name.title()}")
            return

        book.quantity += 1
        self.borrowed_books[user.id].remove(book.id)
        print(f"{user.full_name.title()} has returned {book.name.title()} successfully")

    def print_borrowed_users(self) -> None:
        if not self.borrowed_books:
            print("There are no borrowed books")
            return

        for user_id, borrowed_books_id in self.borrowed_books.items():
            if len(borrowed_books_id) != 0:
                user_name = self.users[user_id].full_name
                book_names = []
                for book_id in borrowed_books_id:
                    book = self.books[book_id]
                    book_names.append(book.name.title())
                print(f"{user_name}: {', '.join(book_names)}")

    def print_users(self) -> None:
        lst_of_users = []
        if not self.users:
            print("There are no Users")
            return
        for user in self.users.values():
            lst_of_users.append(user.full_name.title())
        print("\n".join(lst_of_users))