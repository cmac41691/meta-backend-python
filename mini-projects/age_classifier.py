# Age Classifier
# Demonstrates input handling, type casting, and conditional logic
age = int(input("Enter in your age: ").strip())

if age <= 12:
    demograph = "Child"
elif age <= 17:
    demograph = "Teen"
elif age <= 64:
    demograph = "Adult"
else:
    demograph = "Senior"

print(f"You are a: {demograph}")
