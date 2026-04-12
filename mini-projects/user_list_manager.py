
# user_list_manager.py
# Module: 02 - Functions and Data Structures

# PURPOSE:
# Simulates backend logic for managing users via CLI

# FLOW:
# Input → Validate → Store → Display
# version 1.2

# empty list
users = []

# add user function that appends
def add_user():
    user = input("Enter in a username: ").strip()

    if user == "":
        print("Username must have characters")
        return

    if user in users:
        print("That username already exist")
        return

    users.append(user) 

# display the users
def show_users():
    print(users)

while True:
    # actions for the user to do
    action = input("add / show / exit: ").strip()

    if action == "add":
        add_user()

    elif action == "show":
        show_users()

    elif action == "exit":
        break

    else:
        print("Incorrect")