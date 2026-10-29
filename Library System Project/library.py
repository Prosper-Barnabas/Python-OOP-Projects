from admin import *

class Library:
    def __init__(self) -> None:
        self.admin = Admin()

    def print_menu(self):
        print("\n------- Welcome to the Library ---------\n")
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
        ]
        print("\n".join(options))
        return self.get_choice(len(options))

    def input_is_valid(self, msg, start, end):
        inp = input(msg)

        if not inp.isdecimal:
            print(f"Input a num from {start} to {end}")
            return

    def get_choice(self, num_options: int):
        msg = f"\nEnter your choice from 1 to {num_options}: \n"
        return self.input_is_valid(msg, 1, num_options)

    def add_book(self):
        book_id = int(input("Enter the Book ID: "))
        book_name = input("Enter the Book name: ")
        book_quantity = int(input("Enter the Book quantity: "))
        self.admin.add_books(book_id, book_name, book_quantity)

    def search_book(self):
        pass

    def add_user(self):
        pass

    def search_user(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def print_books(self):
        self.admin.print_books()

    def print_users(self):
        pass

    def print_borrowed_books(self):
        pass

    def run(self):
        is_running = True
        while is_running:
            choice = self.print_menu()

            if choice == 1:
                return self.add_book()
            else:
                print("Exiting the program ...")
                is_running = False

lib = Library()
lib.run()