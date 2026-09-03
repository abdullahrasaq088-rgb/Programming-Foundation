# Build a list of 5 patient names
patients = ["Ahmed", "Abdullah", "General", "Eminent", "Mahbub"]

# Add one patient to the end
patients.append("Aisha")

# Insert one patient
patients.insert(2, "Khadijah")

# Remove one patient
patients.remove("General")

# Print the final count
print("Final count:", len(patients))

# Print the last item
print("Last item:", patients[-1])