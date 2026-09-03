name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

floatbmi = weight / (height * height)

print(name, "your BMI is", round(floatbmi, 2))