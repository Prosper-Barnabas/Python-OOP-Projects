class BankAccount:
    def __init__(self, account_name: str, account_number: str) -> None:
        self.account_name = account_name
        self.account_number = account_number
        self.__balance = 0


    def deposit(self, amount: int):
        if not amount > 0:
            print("Amount to be deposited can't be negative or zero")
            return

        self.__balance += amount
        print(f"${amount} deposited successfully.")


bank = BankAccount("Prosper", "1")
bank.deposit(0)
