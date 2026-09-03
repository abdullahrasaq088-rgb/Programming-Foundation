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


acc_1 = Account("1002345678","John Doe","Savings",150000)
print(acc_1.displayAccount())

acc_2 = Account( "1002345679","Mary Johnson","Current",300000)
print(acc_2.displayAccount())

acc_3 = Account("1002345680", "David Smith","Savings",200000)
print(acc_3.displayAccount())

acc_4 = Account("1002345681","Sarah Williams", "Savings", 500000)
print(acc_4.displayAccount())

acc_5 = Account("1002345682","Michael Brown","Current",750000)
print(acc_5.displayAccount())
