cart_total = 150
is_loyalty_member = True

if cart_total >= 100 and is_loyalty_member:
    discount_percentage = 20
elif cart_total >= 100:
    discount_percentage = 15
elif is_loyalty_member:
    discount_percentage = 5
else:
    discount_percentage = 0

discount_amount = cart_total * (discount_percentage / 100)
final_amount = cart_total - discount_amount

if final_amount < 20:
    final_amount = final_amount + 4.99

print("Cart Total: $", cart_total)
print("Discount: $", discount_amount)
print("Final Amount: $", final_amount)