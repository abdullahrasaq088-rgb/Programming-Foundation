int b = 0;
do {
    Console.WriteLine(b);
    b++;
}
while(b < 5);

int b = 0;
while(b < 5){
    Console.WriteLine(b);
    b++;
}
Console.Write("Enter a number ");
int num = int.Parse(Console.ReadLine()!);
int total;

for (int i = 1; i < 21; i++)
{
    total = num * i;
    Console.WriteLine(total);
}
