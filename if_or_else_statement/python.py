age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ")
number_of_tickets = int(input("How many tickets do you want? "))

if age < 12:
    ticket_price = 8
elif age <= 64:
    ticket_price = 14

    if student == "yes":
        ticket_price = ticket_price - 2
else:
    ticket_price = 10

    if student == "yes":
        ticket_price = ticket_price - 2

total_cost = ticket_price * number_of_tickets

print("Price per ticket: $", ticket_price)
print("Total cost: $", total_cost)