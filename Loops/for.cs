Console.Write("Enter a number ");
int num = int.Parse(Console.ReadLine()!);
int total;
for (int i = 1; i < 21; i++)
{
    total = num * i;
    Console.WriteLine(total);
}
