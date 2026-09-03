Console.Write("Enter your name: ");
string name = Console.ReadLine();

Console.Write("Enter your weight in kg: ");
double weight = double.Parse(Console.ReadLine());

Console.Write("Enter your height in meters: ");
double height = double.Parse(Console.ReadLine());

double bmi = weight / (height * height);

Console.WriteLine(name + " your BMI is " + bmi.ToString("F1"));