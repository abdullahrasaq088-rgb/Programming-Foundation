Console.Write("Enter your age: ");
int age = int.Parse(Console.ReadLine());

Console.Write("Are you a student? (yes/no): ");
string student = Console.ReadLine();

double ticketPrice;

if (age < 12)
{
    ticketPrice = 8;
}
else if (age <= 64)
{
    ticketPrice = 14;

    if (student == "yes")
    {
        ticketPrice = ticketPrice - 2;
    }
}
else
{
    ticketPrice = 10;

    if (student == "yes")
    {
        ticketPrice = ticketPrice - 2;
    }
}

Console.WriteLine("Your ticket price is: $" + ticketPrice);