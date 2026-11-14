class Book:
    def __init__(self, book_id: int, name: str, author: str, quantity: int) -> None:
        self.id = book_id
        self.name = name
        self.author = author
        self.__quantity = quantity

    def __repr__(self) -> str:
        return f"Book({self.id}, {self.name}, {self.author}, {self.__quantity})"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "quantity": self.__quantity,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["name"], data["author"], data["quantity"])

    @property
    def quantity(self) -> int:
        return self.__quantity

    def borrow(self) -> None:
        if self.__quantity <= 0:
            raise ValueError(f"{self.name} is not available")

        self.__quantity -= 1

    def return_book(self) -> None:
        self.__quantity += 1
