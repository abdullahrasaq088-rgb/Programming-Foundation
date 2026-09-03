// Print numbers 1 to 20
for (let number = 1; number <= 20; number++) {

    // Skip multiples of 3
    if (number % 3 === 0) {
        continue;
    }

    // Stop at the first multiple of 7
    if (number % 7 === 0) {
        break;
    }

    // Print the remaining numbers
    console.log(number);
}