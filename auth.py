import json
import os
import re
import bcrypt

USER_FILE = "data/users.json"

if not os.path.exists(USER_FILE):
    os.makedirs("data", exist_ok=True)

    with open(USER_FILE, "w") as file:
        json.dump([], file)

def valid_password(password):
    pattern = r'^[A-Z].*[@#$%^&+=!].*\d+$'
    return re.match(pattern, password)

def register():
    print("\n===== REGISTER =====")
    username = input("Create Username: ").strip()
    password = input("Create Password: ").strip()
    if not valid_password(password):
        print("\nPassword Rules:")
        print("1. First letter must be uppercase")
        print("2. Must contain one special character")
        print("3. Must end with numbers")
        continue_registration = input("Do you want to try again? (y/n): ").strip().lower()
        if continue_registration == 'y':
            return register()

    with open(USER_FILE, "r") as file:
        users = json.load(file)

    for user in users:
        if user["username"] == username:
            print("\nUsername already exists!")
            return False, None
        
    users.append({
        "username": username,
        "password": bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
).decode()
    })

    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)
    return True, username

def login():
    print("\n===== LOGIN =====")
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    with open(USER_FILE, "r") as file:
        users = json.load(file)

    for user in users:
        if (
            user["username"] == username and
            bcrypt.checkpw(
                password.encode(),
                user["password"].encode()
            )
        ):
            print("\nLogin Successful!")
            return username

    print("\nInvalid Username or Password!")
    return None