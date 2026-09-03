class Account:
    def __init__(self, accountNumber, accountName, accountType, balance):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.accountType = accountType
        self.balance = balance

    def displayAccount(self):
        print("="*20)
        print("ACCOUNT INFORMATION")
        print("="*20)
        print("Account Number:", self.accountNumber)
        print("Account Name:", self.accountName)
        print("Account Type:", self.accountType)
        print("Balance: ₦", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def checkBalance(self):
        print(self.accountName, "'s current balance is ₦", self.balance)


account1 = Account("1002345678", "John Doe", "Savings", 150000)
account2 = Account("1002345679", "Mary Johnson", "Current", 300000)
account3 = Account("1002345680", "David Smith", "Savings", 200000)
account4 = Account("1002345681", "Grace Williams", "Current", 250000)
account5 = Account("1002345682", "Peter Brown", "Savings", 180000)

account1.checkBalance()
account2.checkBalance()
account3.checkBalance()
account4.checkBalance()
account5.checkBalance()