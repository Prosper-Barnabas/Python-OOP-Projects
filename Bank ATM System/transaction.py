from datetime import datetime


class Transaction:
    def __init__(self, amount, transaction_type) -> None:
        self.amount = amount
        self.timestamp = datetime.now()

        permitted_transaction_types = ("deposit", "withdrawal")
        if transaction_type not in permitted_transaction_types:
            print(f"{transaction_type} is not a transaction type")
            return
        self.transaction_type = transaction_type

    def __repr__(self) -> str:
        return f"{self.transaction_type}, {self.amount}, {self.timestamp}"

    def __str__(self) -> str:
        return f"{self.transaction_type.capitalize()}: ${self.amount} at {self.timestamp}"
