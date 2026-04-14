
# user_list_manager.py
# Module: 02 - Functions and Data Structures

# PURPOSE:
# Simulates backend logic for managing users via CLI

# FLOW:
# Input → Validate → Store → Display
# version 1.2

# empty list
users = [
    {"username": "coady", "role": "user"},
    {"username": "iain", "role": "user"}
]

# add user function that appends
def add_user():
    username = input("Enter in a username: ").strip()

    if username == "":
        print("Username must have characters")
        return

    for user in users:
        if user["username"] == username:
            print("That name has been taken, pick another one")
            return

    new_user = {
        "username": username,
        "role": "user"
    }

    users.append(new_user)
    print("User has been added successfully")

# display the users
def show_users():
    if not users:
        print("No users found")
        return

    for user in users:
        print(user["username"])

while True:
    # actions for the user to do
    action = input("add / show / exit: ").strip().lower()

    if action == "add":
        add_user()

    elif action == "show":
        show_users()

    elif action == "exit":
        break

    else:
        print("Incorrect")