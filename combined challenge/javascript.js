const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let balance = 1250.00;

rl.question("Enter withdrawal amount: ", function(input) {

    let withdrawal = parseFloat(input);

    if (withdrawal <= 0) {
        console.log("Invalid withdrawal amount.");
    }
    else if (withdrawal > balance) {
        console.log("Insufficient balance.");
    }
    else if (withdrawal % 10 !== 0) {
        console.log("ATM only dispenses multiples of $10.");
    }
    else {
        balance = balance - withdrawal;

        if (balance < 20) {
            console.log("Warning: Your remaining balance is below $20.");
        }

        console.log("Withdrawal successful.");
        console.log("New balance: $" + balance);
    }

    rl.close();
});