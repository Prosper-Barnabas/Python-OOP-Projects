import json

from pathlib import Path

from book import Book
from student import Student

DATA_FILE = Path(__file__).parent / "library.json"

class Library_Manager:
    def __init__(self) -> None:
        self.books = {}
        self.students = {}
        self.borrowed_books = {}

        self.load_state()

    def add_books(
        self, book_id: int, book_name: str, book_author: str, book_qty: int
    ) -> None:
        existing_books = [book.name for book in self.books.values()]
        if book_name.title() in existing_books:
            print(f"{book_name.title()} already exists")
            return
        if book_id in self.books:
            print(f"Book ID: {book_id} already exists")
            return
        current_id = [book.id for book in self.books.values()]
        print(max(current_id))
        #if int(book_id) > current_id:
        #    print(f"Previous ID: {}, Input {}")
        new_book = Book(book_id, book_name.title(), book_author.title(), book_qty)
        self.books[book_id] = new_book
        self.save_state()
        print(f"\n{book_name.title()} added successfully")

    def print_books(self) -> None:
        lst_of_books = []
        if not self.books:
            print("There are no books")
            return
        for book in self.books.values():
            lst_of_books.append((book.name, book.id, book.quantity))
        print(
            "\n".join(
                f"Name: {book[0]}, ID: {book[1]}, Quantity: {book[2]}"
                for book in lst_of_books
            )
        )

    def search_book(self, query: int | str) -> str | None:
        if isinstance(query, int):
            found_books = [
                (book.name, book.author) for book in self.books.values() if query == book.id
            ]
        elif isinstance(query, str):
            found_books = [
                book.author
                for book in self.books.values()
                if query.lower() in book.name.lower()
                or query.lower() in book.author.lower()
            ]

        if not found_books:
            print("No book matched your search.")
            return

        return "\n".join(f"{book[0]} by {book[1]}" for book in found_books)

    def add_student(self, student_id: int, student_fname: str, student_lname: str) -> None:
        student_full_name = student_fname.title() + " " + student_lname.title()
        existing_students = [student.full_name for student in self.students.values()]
        if student_id in self.students:
            print(f"student ID: {student_id} already exists")
            return
        if student_full_name.title() in existing_students:
            print(f"{student_full_name} already exists")
            return
        new_student = Student(student_id, student_fname.title(), student_lname.title())
        self.students[student_id] = new_student
        self.save_state()
        print(f"\n{student_full_name} added successfully")

    def search_student(self, query: int | str) -> str | None:
        if isinstance(query, int):
            found_students = [
                student.full_name for student in self.students.values() if query == student.id
            ]
        elif isinstance(query, str):
            found_students = [
                student.full_name.title()
                for student in self.students.values()
                if query.lower() in student.full_name.lower()
            ]
        if not found_students:
            print("No student matched your search.")
            return

        return "\n".join(found_students)

    def borrow_book(self, book_name: str, student_name: str):
        book = None
        for current_book in self.books.values():
            if current_book.name == book_name.title():
                book = current_book
                break

        if book is None or book.quantity <= 0:
            print(f"Book: {book_name.title()} is not available")
            return

        student = None
        for current_student in self.students.values():
            if current_student.full_name == student_name.title():
                student = current_student
                break

        if student is None:
            print(f"student: {student_name.title()} is not found")
            return

        if student.id not in self.borrowed_books:
            self.borrowed_books[student.id] = []

        if book.id in self.borrowed_books[student.id]:
            print(f"{student.full_name} has already borrowed {book.name}")
            return

        self.borrowed_books[student.id].append(book.id)
        book.quantity -= 1
        self.save_state()
        print(f"{student.full_name} borrowed {book.name}")

    def return_book(self, book_name: str, student_name: str):
        book = None
        for current_book in self.books.values():
            if current_book.name == book_name.title():
                book = current_book
                break

        if book is None:
            print(f"Book: {book_name.title()} is not available")
            return

        student = None
        for current_student in self.students.values():
            if current_student.full_name == student_name.title():
                student = current_student
                break

        if student is None:
            print(f"student: {student_name.title()} is not found")
            return

        if student.id not in self.borrowed_books:
            print(f"{student.full_name} has not borrowed any book")
            return

        if book.id not in self.borrowed_books[student.id]:
            print(f"{student.full_name} did not borrow {book.name}")
            return

        book.quantity += 1
        self.borrowed_books[student.id].remove(book.id)
        self.save_state()
        print(f"{student.full_name} has returned {book.name} successfully")

    def print_borrowed_students(self) -> None:
        if not self.borrowed_books:
            print("There are no borrowed books")
            return

        for student_id, borrowed_books_id in self.borrowed_books.items():
            if len(borrowed_books_id) != 0:
                student_name = self.students[student_id].full_name
                book_names = []
                for book_id in borrowed_books_id:
                    book = self.books[book_id]
                    book_names.append(book.name.title())
                print(f"{student_name}: {', '.join(book_names)}")

    def print_students(self) -> None:
        lst_of_students = []
        if not self.students:
            print("There are no students")
            return
        for student in self.students.values():
            lst_of_students.append((student.id, student.full_name.title()))
        print(
            "\n".join(f"ID: {student[0]}, student Name: {student[1]}" for student in lst_of_students)
        )

    def load_state(self):
        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                state = json.load(file)
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            return

        for book_data in state.get("books", []):
            try:
                book = Book.from_dict(book_data)
            except (TypeError, ValueError, KeyError) as error:
                print(f"Skipping invalid book record: {error}")
            self.books[book.id] = book

        for student_data in state.get("students", []):
            student = Student.from_dict(student_data)
            self.students[student.id] = student

        self.borrowed_books = {
            int(student_id): book_ids
            for student_id, book_ids in state.get("borrowed_books", {}).items()
        }

    def save_state(self):
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(self.get_state(), file, indent=4)

    def get_state(self) -> dict:
        return {
            "books": [book.to_dict() for book in self.books.values()],
            "students": [student.to_dict() for student in self.students.values()],
            "borrowed_books": self.borrowed_books,
        }
