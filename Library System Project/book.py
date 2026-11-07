class Book:
    def __init__(self, id: int, name: str, quantity: int) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Book({self.id}, {self.name}, {self.quantity})"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["id"],
            data["name"],
            data["quantity"],
        )
