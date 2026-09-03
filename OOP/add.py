from phone import *

addition_1 = Arithmetic(10, 5)   
addition_2 = Arithmetic(20, 4)
subtraction_1 = Arithmetic(15, 3)   
print("Addition:", addition_1.add())
print("Subtraction:", addition_1.subtract())
print("Multiplication:", addition_1.multiply())
print("Division:", addition_1.divide())

kuto = office("Kuto Office", "Lagos")
print(kuto.get_info())
print(kuto.get_staff_count(50))