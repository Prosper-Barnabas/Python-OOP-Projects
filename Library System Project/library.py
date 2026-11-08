from admin import *


class Library:
    def __init__(self) -> None:
        self.admin = Admin()

    # helper function to give the user a retry for errors involving numbers
    def get_integer(self, prompt: str, minimum: int | None = None) -> int:
        while True:
            value = input(prompt)

            try:
                number = int(value)
            except ValueError:
                print("Please enter a valid whole number")
                continue

            if minimum is not None and number < minimum:
                print(f"Please enter a number greater than {minimum}")
                continue

            return number

    def print_menu(self):
        print("\n\n------- Welcome to the Library ---------\n")
        options = [
            "1) Add Book",
            "2) Search Book",
            "3) Add User",
            "4) Search User",
            "5) Borrow Book",
            "6) Return Book",
            "7) Print Books",
            "8) Print Users",
            "9) Print Borrowed Books",
            "0) Exit the Program ..."
        ]
        print("\n".join(options))
        return self.get_choice(len(options) - 1)

    # helper function to get the choice of menu from the user
    def get_choice(self, num_options: int) -> int | None:
        msg = input(f"\nEnter your choice from 0 to {num_options}:\n")
        if not msg.isdecimal() or int(msg) > num_options or int(msg) < 0:
            print(f"Invalid input. Pls put in a number between 1 and {num_options}")
            return
        return int(msg)

    def add_book(self):
        book_id = self.get_integer("Enter the Book ID: ", 1)
        book_name = input("Enter the Book name: ")
        book_quantity = self.get_integer("Enter the Book quantity: ", 0)
        self.admin.add_books(book_id, book_name, book_quantity)

    def search_book(self):
        query = input("Enter the Book ID or name: ")
        if query.isdecimal():
            query = int(query)
        print("\nSearching for book ...")
        print(self.admin.search_book(query))

    def add_user(self):
        user_id = self.get_integer("Enter the User's ID: ", 1)
        user_fname = input("Enter the User's First name: ")
        user_lname = input("Enter the User's Last name: ")
        self.admin.add_user(user_id, user_fname, user_lname)

    def search_user(self):
        query = input("Enter the User ID or name: ")
        if query.isdecimal():
            query = int(query)
        print("Searching for User ...")
        print(self.admin.search_user(query))

    def borrow_book(self):
        book_name = input("Enter the Book name: ")
        user_name = input("Enter the User name: ")
        return f"\n{self.admin.borrow_book(book_name, user_name)}"

    def return_book(self):
        book_name = input("Enter the Book name: ")
        user_name = input("Enter the User name: ")
        return f"\n{self.admin.return_book(book_name, user_name)}"

    def print_books(self):
        print("\nList of books in the library:\n")
        self.admin.print_books()

    def print_users(self):
        print("\nList of Users in the library:\n")
        self.admin.print_users()

    def print_borrowed_books(self):
        print("\nList of borrowed books\n")
        self.admin.print_borrowed_users()

    def run(self):
        is_running = True
        while is_running:
            choice = self.print_menu()

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.search_book()
            elif choice == 3:
                self.add_user()
            elif choice == 4:
                self.search_user()
            elif choice == 5:
                self.borrow_book()
            elif choice == 6:
                self.return_book()
            elif choice == 7:
                self.print_books()
            elif choice == 8:
                self.print_users()
            elif choice == 9:
                self.print_borrowed_books()
            elif choice == 0:
                print("Exiting the program ...")
                is_running = False