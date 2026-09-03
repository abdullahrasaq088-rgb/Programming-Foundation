string full_name = "Rasaq Abdullah";
int age = 25;
double hourly_wage = 15.50;
bool is_full_time = true;

Console.WriteLine("Employee: " + full_name);
Console.WriteLine("Age: " + age);
Console.WriteLine("Hourly Wage: $" + hourly_wage);
Console.WriteLine("Full-Time: " + is_full_time);

if (is_full_time) 
{
    double Weekly_pay = hourly_wage * 40;
    Console.WriteLine("Estimated Weekly Pay: $", Weekly_pay);
}
