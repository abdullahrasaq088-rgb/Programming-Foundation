const readline = require("readline");

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.question("Enter your name: ", function(name) {
	rl.question("Enter your weight in kg: ", function(weightInput) {
		rl.question("Enter your height in meters: ", function(heightInput) {
			const weight = parseFloat(weightInput);
			const height = parseFloat(heightInput);
			const bmi = weight / (height * height);

			console.log(name + " your BMI is " + bmi.toFixed(1));
			rl.close();
		});
	});
});