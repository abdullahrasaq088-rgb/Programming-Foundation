var patients = new List<string>
  { "Ahmed", "Abdullah", "General", "Eminent", "Mahbub" };
 
// Add / remove
patients.Add("Aisha"); 
// Insert one patient
patients.Insert(2, "Khadijah");

//remove one patient
patients.Remove("General");

// Print the final count
Console.WriteLine(patients.Count);

// Print the last item
Console.WriteLine("Last item: " + patients[patients.Count - 1]);