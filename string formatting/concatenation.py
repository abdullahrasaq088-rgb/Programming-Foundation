name = "Ademide"
print(len(name))  # Output: 7
print(name.upper())  # Output: ADEMIDE
print(name.lower())  # Output: ademide
print(name.capitalize())  # Output: Ademide
print(name.replace("A", "E"))  # Output: Edemide
print(name.split("e"))  # Output: ['Ad', 'mid', '']
print(name.startswith("A"))  # Output: True
print(name.endswith("e"))  # Output: True
print(name.find("m"))  # Output: 3
print(name.count("e"))  # Output: 2
print(name.isalpha())  # Output: True
print(name.isdigit())  # Output: False
print(name.isalnum())  # Output: True
print(name.strip())  # Output: Ademide
print(name.center(20, "*"))  # Output: *******Ademide*******
print(name.ljust(20, "+"))  # Output: Ademide-------------
print(name.rjust(20, "#"))  # Output: -------------Ademide
print(name.casefold())  # Output: ademide