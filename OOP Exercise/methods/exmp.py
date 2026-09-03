class Account:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def checkBalance(self):
        print(f"{self.account_name}'s balance: {self.balance}")


acc_1 = Account("1002345678", "John Doe", 150000)
acc_2 = Account("1002345679", "Mary Johnson", 300000)
acc_3 = Account("1002345680", "David Smith", 200000)

acc_1.deposit(50000)
acc_2.deposit(50000)
acc_3.deposit(50000)

acc_1.checkBalance()
acc_2.checkBalance()
acc_3.checkBalance()