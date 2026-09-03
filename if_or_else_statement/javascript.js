const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter your age: ", function(ageInput) {

    rl.question("Are you a student? (yes/no): ", function(student) {

        let age = parseInt(ageInput);
        let ticketPrice;

        if (age < 12) {
            ticketPrice = 8;
        } 
        else if (age <= 64) {
            ticketPrice = 14;

            if (student === "yes") {
                ticketPrice = ticketPrice - 2;
            }
        } 
        else {
            ticketPrice = 10;

            if (student === "yes") {
                ticketPrice = ticketPrice - 2;
            }
        }

        console.log("Your ticket price is: $" + ticketPrice);

        rl.close();
    });
});