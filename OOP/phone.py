#surfing OOP concepts in Python
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"


phone_one =Phone("Apple", "iPhone 13", 999)
print(phone_one.model)

phone_two = Phone("Samsung", "Galaxy S21", 799)
print(phone_two.model)

phone_one = Phone("Apple", "iPhone 13", 999)
print(phone_one.make_call(1234567890))    

class Arithmetic:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero is not allowed."
addition_1 = Arithmetic(10, 5)
print("Addition:", addition_1.add())
print("Subtraction:", addition_1.subtract())
print("Multiplication:", addition_1.multiply())
print("Division:", addition_1.divide())

class office:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f"Office Name: {self.name}, Location: {self.location}"

    def get_staff_count(self, count):
        return f"Staff Count: {count}"
    def get_customer_info(self, customer_name, customer_id):
        return f"Customer Name: {customer_name}, Customer ID: {customer_id}"
     
arigbajo_office = office("Arigbajo Office", "Lagos")
print(arigbajo_office.get_info())
#print(arigbajo_office.get_staff_count(50))
#print(arigbajo_office.get_customer_info("John Doe", "CUST001")) 

ifo_office = office("IFO Office", "Ibadan")
print(ifo_office.get_info())

ikorodu_office = office("Ikorodu Office", "Lagos")
print(ikorodu_office.get_info())

idumata_office = office("Idumata Office", "Lagos")
print(idumata_office.get_info())


