class Bank:
    def __init__(self, bankName, branch, manager, numberOfEmployees):
        self.bankName = bankName
        self.branch = branch
        self.manager = manager
        self.numberOfEmployees = numberOfEmployees

    def displayBank(self):
        print("=" * 30)
        print("BANK INFORMATION")
        print("=" * 30)
        print("Bank Name:", self.bankName)
        print("Branch:", self.branch)
        print("Manager:", self.manager)
        print("Number of Employees:", self.numberOfEmployees)

    def changeManager(self, newManager):
        self.manager = newManager

    def updateEmployeeCount(self, number):
        self.numberOfEmployees = number

bank1 = Bank("First Bank", "Lagos", "Mr. Ade", 50)
bank2 = Bank("Access Bank", "Abuja", "Mrs. Bello", 70)
bank3 = Bank("GTBank", "Ibadan", "Mr. Okafor", 60)

bank1.changeManager("Mr. Yusuf")
bank2.changeManager("Mrs. Fatima")

bank1.updateEmployeeCount(55)
bank2.updateEmployeeCount(80)

bank1.displayBank()
bank2.displayBank()
bank3.displayBank()