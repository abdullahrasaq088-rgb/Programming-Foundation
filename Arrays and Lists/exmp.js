// Build an array of 5 patient names
let patients = ["Ahmed", "Abdullah", "General", "Eminent", "David"];

// Add one patient to the end
patients.push("Aisha");

// Insert one patient
patients.unshift("Khadijah");

// Remove one patient
patients.splice(patients.indexOf("General"), 1);

// Print the final count
console.log("Final count:", patients.length);

// Print the last item
console.log("Last item:", patients[patients.length - 1]);