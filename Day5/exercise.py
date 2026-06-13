person = {"name": "Mao", "age": 22, "courses": ["Math", "Computer Science"], "grade": "A"}
print(person)
person ["address"] = "123 Main St"  # Adding Key-Value Pairs
#Updating Values
person ["age"]=23

if "grade" in person:
    del person["grade"]  # Removing Key-Value Pairs if exists

print(person)
