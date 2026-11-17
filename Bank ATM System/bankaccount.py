class BankAccount:
    def __init__(self, account_name: str, account_number: str) -> None:
        self.account_name = account_name
        self.account_number = account_number
        self.__balance = 0

bank = BankAccount("Prosper", "1")