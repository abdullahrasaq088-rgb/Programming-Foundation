double balance = 1250.00;

Console.Write("Enter withdrawal amount: ");
double withdrawal = double.Parse(Console.ReadLine());

if (withdrawal <= 0)
{
    Console.WriteLine("Invalid withdrawal amount.");
}
else if (withdrawal > balance)
{
    Console.WriteLine("Insufficient balance.");
}
else if (withdrawal % 10 != 0)
{
    Console.WriteLine("ATM only dispenses multiples of $10.");
}
else
{
    balance = balance - withdrawal;

    if (balance < 20)
    {
        Console.WriteLine("Warning: Your remaining balance is below $20.");
    }

    Console.WriteLine("Withdrawal successful.");
    Console.WriteLine("New balance: $" + balance);
}