# Create a patient record
patient = {
    "name": "Ahmed",
    "age": 35,
    "ward": "Ward A",
    "diagnosis": "Malaria"
}

# Update ward
patient["ward"] = "Ward B"

# Add admittedDate
patient["admittedDate"] = "2026-09-01"

# Safely check before printing diagnosis
if "diagnosis" in patient:
    print("Diagnosis:", patient["diagnosis"])
else:
    print("Diagnosis not available")