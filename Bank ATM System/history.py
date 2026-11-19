from transaction import Transaction

class TransactionHistory:
    def __init__(self) -> None:
        self.__transactions = []

    def add_transaction(self, transaction: Transaction) -> None:
        if not isinstance(transaction, Transaction):
            print(f"{transaction} is not a valid Transaction")
            return
        self.__transactions.append(transaction)

    def get_transactions(self):
        return self.__transactions.copy()

    def display_transactions(self):
        if len(self.__transactions) == 0:
            print("No transactions yet.")
            return
        for transaction in self.__transactions:
            print(transaction)