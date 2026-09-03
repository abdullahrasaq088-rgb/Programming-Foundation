Console.Write("Enter a grade: ");
string grade = Console.ReadLine()!;
switch (grade)
{
    case "A":
        Console.Write("4.0");
    break;
    case "B":
        Console.Write("3.0");
    break;
    case "C":
        Console.Write("2.0");
    break;
    case "D":
        Console.Write("1.0");
    break;
    case "F":
        Console.Write("0.0");
        break;
    default:
        Console.Write("You entered an invalid grade");
        break;
}
