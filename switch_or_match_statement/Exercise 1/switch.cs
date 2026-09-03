Console.Write("Enter a day number (1-7) : ");
int day = int.Parse(Console.ReadLine()!);
switch (day)
{
    case 1:
        Console.Write("Monday");
        break;
    case 2:
        Console.Write("Tuesday");
        break;
    case 3:
        Console.Write("Wednesday");
        break;
    case 4:
        Console.Write("Thursday");
        break;
    case 5:
        Console.Write("Friday");
        break;
    case 6:
        Console.Write("Saturday");
        break;
    case 7:
        Console.Write("Sunday");
        break;
    Default:
        Console.Write("you entered an invalid number");
}