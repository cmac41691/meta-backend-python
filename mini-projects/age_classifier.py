# Age Classifier
# Demonstrates input handling, type casting, and conditional logic

while True:
    print("##|##| MENU ##|##|")
    print("1. Hello")
    print("2. Age Classifier")
    print("3. Exit")

    choice = input("Choose an option: ").strip().lower()

    match choice:
        case "1":
            print("Hello")

        case "2":
            # VALIDATION LOOP
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

            # CLASSIFICATION
            if age <= 12:
                demograph = "Child"
            elif age <= 17:
                demograph = "Teen"
            elif age <= 64:
                demograph = "Adult"
            else:
                demograph = "Senior"

            print(f"You are a: {demograph}")

        case "3":
            print("Exit")
            break

        case _:
            print(f"Invalid choice '{choice}'. Please pick from menu.")