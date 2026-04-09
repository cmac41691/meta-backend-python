# Age Classifier
# Demonstrates input handling, type casting, and conditional logic

# attempt 2 (fixed)

while True:
    age = input("Enter in your age: ").strip()

    if age == "":
        print("Error")
        continue

    age = int(age)

    if age < 0:
        print("Error")
        continue

    break



if age <= 12:
    demograph = "Child"
elif age <= 17:
    demograph = "Teen"
elif age <= 64:
    demograph = "Adult"
else:
    demograph = "Senior"

print(f"You are a: {demograph}")
