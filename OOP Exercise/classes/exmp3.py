class Customer:
    def __init__(self, customerId, name, email, phone):
        self.customerId = customerId
        self.name = name
        self.email = email
        self.phone = phone

    def displayCustomer(self):
        print("==============================")
        print("CUSTOMER INFORMATION")
        print("==============================")
        print("Customer ID:", self.customerId)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)