let full_name = "Rasaq Abdullah";
let age = 25;
let hourly_wage = 15.50;
let is_full_time = true;

console.log("Employee:", full_name);
console.log("Age:", age);
console.log("Hourly Wage: $", hourly_wage);
console.log("Full-Time:", is_full_time);

if (is_full_time) {
    let Weekly_pay = hourly_wage * 40;
    console.log("Estimated Weekly Pay: $", Weekly_pay);
}