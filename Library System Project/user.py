class User:
    def __init__(self, id: int, first_name: str, last_name: str) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name

    def __repr__(self) -> str:
        return f"User({self.id}, {self.first_name}, {self.last_name})"