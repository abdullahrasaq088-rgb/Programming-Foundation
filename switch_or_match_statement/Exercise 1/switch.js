const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter a day number (1-7): ", (day) => {
switch (day.trim()) {
    case "1":
        console.log("Monday");
    break;
    case "2":
        console.log("Tuesday");
    break;
    case "3":
        console.log("Wednesday");
    break;
    case "4":
        console.log("Thursday");
    break;
    case "5":
    console.log("Friday");
    break;
    case "6":
        console.log("Saturday");
    break;
    case "7":
        console.log("Sunday");
        break;
    default:
        console.log("You entered an invalid number");
}
rl.close();
});