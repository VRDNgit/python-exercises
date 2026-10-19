class BankAccount:
    total_accounts = 0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            return self.balance
        else:
            return "Invalid amount"

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def is_valid_amount(amount):
        if amount > 0:
            return True
        else:
            return False