from transaction import Transaction
from history import TransactionHistory

class BankAccount:
    def __init__(self, account_name: str, account_number: str) -> None:
        self.account_name = account_name
        self.account_number = account_number
        self.__balance: int = 0
        self.__history = TransactionHistory()

    def deposit(self, amount: int) -> None:
        if not amount > 0:
            print("Amount must be greater than 0")
            return

        self.__balance += amount
        successful_transaction = Transaction(amount, "deposit")
        self.__history.add_transaction(successful_transaction)
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        if amount > self.__balance:
            print("Insufficient Balance")
            return

        self.__balance -= amount
        successful_transaction = Transaction(amount, "withdrawal")
        self.__history.add_transaction(successful_transaction)
        print(f"${amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance

    def get_transaction_history(self):
        return self.__history.get_transactions()

bank = BankAccount("Prosper Barnabas", "1")
bank.deposit(100)
bank.withdraw(40)
bank.get_balance()