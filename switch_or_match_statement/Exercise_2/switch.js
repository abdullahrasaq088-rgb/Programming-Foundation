const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter a grade: ", (grade) =>{
switch (grade.trim()){
    case "A":
        console.log("4.0")
    break;
    case "B":
        console.log("3.0")
    break;
    case "C":
    console.log("2.0")
    break;
    case "D":
        console.log("1.0")
    break;
    case "F":
        console.log("0.0")
        break;
    default:
        console.log("You entered an invalid grade")
}
rl.close();
});