class Account:
    def __init__(self, accountNumber, accountName, accountType, balance):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.accountType = accountType
        self.balance = balance

    def displayAccount(self):
        print("="*40)
        print("ACCOUNT INFORMATION")
        print("="*40)
        print("Account Number:", self.accountNumber)
        print("Account Name:", self.accountName)
        print("Account Type:", self.accountType)
        print("Balance: ₦", self.balance)
        print("="*40)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

