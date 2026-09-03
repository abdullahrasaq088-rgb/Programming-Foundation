patient = {
    "name": "Amaka Obi",
    "age": 42,
    "ward": "Oncology"
}
 
print(patient["name"])
print(patient.get("age"))
 
patient["age"] = 43
patient["phone"] = "0803..."
del patient["phone"]
 
print("ward" in patient)
print(len(patient))
