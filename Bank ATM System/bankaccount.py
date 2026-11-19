from transaction import Transaction
from history import TransactionHistory


class BankAccount:
    def __init__(self, account_name: str, account_number: str) -> None:
        self.account_name = account_name
        self.account_number = account_number
        self.__balance: int = 0
        self.__history = TransactionHistory()

    # helper methods
    def _validate_amount(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Amount must be a number")
        if not amount > 0:
            raise ValueError("Amount must be greater than 0")

    def _update_balance(self, amount):
        self.__balance += amount

    def _record_transaction(self, amount, transaction_type):
        successful_transaction = Transaction(amount, transaction_type)
        self.__history.add_transaction(successful_transaction)

    def deposit(self, amount: int) -> None:
        self._validate_amount(amount)
        self._record_transaction(amount, "deposit")
        self._update_balance(amount)
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount: int) -> None:
        self._validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Insufficient Balance")

        self._record_transaction(amount, "withdrawal")
        self._update_balance(-amount)
        print(f"${amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance

    def display_transactions_history(self):
        return self.__history.display_transactions()


class SavingsAccount(BankAccount):
    def __init__(self, account_name: str, account_number: str) -> None:
        super().__init__(account_name, account_number)
        self.min_balance = 100

    def withdraw(self, amount: int) -> None:
        self._validate_amount(amount)
        current_balance = self.get_balance()
        if (current_balance - amount) < self.min_balance:
            raise ValueError(
                f"Transaction declined: This withdrawal would bring your account below the required minimum balance of {self.min_balance}"
            )
        return super().withdraw(amount)


class CheckingAccount(BankAccount):
    def __init__(self, account_name: str, account_number: str) -> None:
        super().__init__(account_name, account_number)
        self.fee: int = 10
        self.limit: int = 100

    def withdraw(self, amount: int) -> None:
        self._validate_amount(amount)
        max_withdrawal = self.limit + self.get_balance()
        if amount > max_withdrawal:
            raise ValueError("Amount is greater than the overdraft")

        self._record_transaction(amount, "withdrawal")
        self._update_balance(-amount)
        if self.get_balance() < 0:
            self._record_transaction(self.fee, "fee")
            self._update_balance(-self.fee)
        print(f"${amount} withdrawn successfully.")
