class Customer:
    def __init__(self, customerId, name, email, phone):
        self.customerId = customerId
        self.name = name
        self.email = email
        self.phone = phone

    def displayCustomer(self):
        print("="*30)
        print("CUSTOMER INFORMATION")
        print("="*30)
        print("Customer ID:", self.customerId)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)

customer1 = Customer("C001", "John Doe", "john@example.com", "08012345678")
customer2 = Customer("C002", "Mary Johnson", "mary@example.com", "08023456789")
customer3 = Customer("C003", "David Smith", "david@example.com", "08034567890")
customer4 = Customer("C004", "Sarah Williams", "sarah@example.com", "08045678901")
customer5 = Customer("C005", "Michael Brown", "michael@example.com", "08056789012")

customer1.displayCustomer()
customer2.displayCustomer()
customer3.displayCustomer()
customer4.displayCustomer()
customer5.displayCustomer()