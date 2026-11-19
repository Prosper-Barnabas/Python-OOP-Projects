from datetime import datetime


class Transaction:
    def __init__(self, amount: int, transaction_type: str) -> None:
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Amount must be a number")
        if not amount > 0:
            raise ValueError("Amount must be greater than zero")

        self.amount = amount

        permitted_transaction_types = ("deposit", "withdrawal")
        if transaction_type not in permitted_transaction_types:
            raise ValueError(f"{transaction_type} is not a transaction type")

        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __repr__(self) -> str:
        return f"{self.transaction_type}, {self.amount}, {self.timestamp}"

    def __str__(self) -> str:
        return f"{self.transaction_type.capitalize()}: ${self.amount} at {self.timestamp.strftime('%d/%m/%Y, %H:%M:%S')}"
