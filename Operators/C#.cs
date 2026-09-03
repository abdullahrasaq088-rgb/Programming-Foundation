double cartTotal = 150;
bool isLoyaltyMember = true;

double discountPercentage;

if (cartTotal >= 100 && isLoyaltyMember)
{
    discountPercentage = 20;
}
else if (cartTotal >= 100)
{
    discountPercentage = 15;
}
else if (isLoyaltyMember)
{
    discountPercentage = 5;
}
else
{
    discountPercentage = 0;
}

double discountAmount = cartTotal * (discountPercentage / 100);
double finalAmount = cartTotal - discountAmount;

if (finalAmount < 20)
{
    finalAmount = finalAmount + 4.99;
}

Console.WriteLine("Cart Total: $" + cartTotal);
Console.WriteLine("Discount: $" + discountAmount);
Console.WriteLine("Final Amount: $" + finalAmount);