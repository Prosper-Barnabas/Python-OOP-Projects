class Book:
    def __init__(self, book_id: int, name: str, author: str, quantity: int) -> None:
        self.id = book_id
        self.name = name
        self.author = author
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Book({self.id}, {self.name}, {self.author}, {self.quantity})"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["name"], data["author"], data["quantity"])
