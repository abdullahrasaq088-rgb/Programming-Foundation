balance = 1250.00

withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Invalid withdrawal amount.")

elif withdrawal > balance:
    print("Insufficient balance.")

elif withdrawal % 10 != 0:
    print("ATM only dispenses multiples of $10.")

else:
    balance = balance - withdrawal

    if balance < 20:
        print("Warning: Your remaining balance is below $20.")

    print("Withdrawal successful.")
    print("New balance: $", balance)