Console.Write("Enter English test score: ");
int test = int.Parse(Console.ReadLine()!);
Console.Write("Enter English Exam score: ");
int exam = int.Parse(Console.ReadLine()!);
int total = test + exam;
switch (total)
{
    case < 40:
        Console.Write("Poor Result");
        break;
    case <= 49:
        Console.Write("Fair");
        break;
    case <= 59:
        Console.Write("Good");
        break;
    case <= 69:
        Console.Write("Very Good");
        break;
    case >= 70:
        Console.Write("Excellent Result");
        break;
}