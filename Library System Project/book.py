class Book:
    def __init__(self, id: int, name: str, quantity: int) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Book({self.id}, {self.name}, {self.quantity})"