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