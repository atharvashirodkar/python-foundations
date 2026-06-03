import json
from pathlib import Path

file_path = Path("data/users_data.json")
backup_file_path = Path("data/user_data_backup.json")

print("Select option by entering respective number")

print("1. Sign-In")
print("2. Sign-Up")

# Sign-Up
def sign_up(username, password):
    user = load_data(username)
    if user:
        print("This username is already taken. Please choose a different username.")

    else:
        while password == "":
            print("please set the password")
            password = input("password: ")
        user = {"password": password}
        with open(file_path, "w") as file:
            json.dump(user, file, indent=4)

        print("Welcome! Your account has been successfully created.")

# Sign-In
def sign_in(username, password):
    user = load_data(username)
    if user:
        if user["password"] == password:
            print("Welcome to the system.")
    else:
        print("Invalid username")


def load_data(username):
    if file_path.exists():
        with open(file_path, "r") as file:
            file_content = json.load(file)
            user = file_content["users"].get(username)

    return user

def main():
    option = input("Enter a number: ")
    while option != "1" and option != "2":
        print("Invalid option selected, try again")

        option = input("Enter a number: ")

    match option:
        case "1":
            print("1. Sign-In")
        case "2":
            print("2. Sign-Up")

    username = input("username: ")
    password = input("password: ")

    if option == "1":
        print(1)
        sign_up(username, password)
    elif option == "2":
        print(2)
        sign_in(username, password)

main()