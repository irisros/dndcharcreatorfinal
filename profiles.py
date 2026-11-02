import json
import os

players = {}
current_player = None

FILE_NAME = "players.json"

def load_players():
    global players
    file_exists = os.path.exists(FILE_NAME)
    if file_exists:
        file = open(FILE_NAME, "r")
        players = json.load(file)
        file.close()
    else:
        players = {}

def safe_players():
    file = open(FILE_NAME, "w")
    json.dump(players, file, indent=4)
    file.close()

def login_password_check():
    global players
    global current_player
    password = players[current_player]["Password"]
    while True:
        password_check = input("Please enter your password: ")
        if password == password_check:
            break
        if password != password_check:
            print("Wrong password. Try again.")
            continue

def check_if_logged_in():
    global current_player
    if current_player is None:
        return True
    else:
        return False

def initialize_player():
    global players
    global current_player
    username = input("What is your username?")
    current_player = username
    if username in players:
        login_password_check()
        profile = players[current_player]
        print(f"""Logged in as {username}""")
    else:
        print("No existing account found. Creating a new account.")
        create_account(username)
        profile = players[current_player]
    return profile

def create_account(username=None):
    global current_player
    global players
    if username is None:
        username = input("What is your username?: ").capitalize()
        if username in players:
            print ("This account already exists. Please use Change Account to log into your existing account, or choose another name.")
            return
    current_player = username
    while True:
        password = input("Create a new password: ")
        check_password = input("Please repeat your password: ")
        if check_password == password:
            print("Password created.")
            break
        if check_password != password:
            print("Please try again")
            continue
    birthdate = input("What is your birthdate, in dd-mm-yyyy?: ")
    gender = input("What is your gender?: ")
    print("Creating profile...")
    create_profile(username, birthdate, gender, password)

def create_profile(username, birthdate, gender, password):
    global players
    players[username] = {
    "Password" : password,
    "Birthdate" : birthdate,
    "Gender" : gender
    }
    safe_players()
    print("Profile created.")

def delete_account():
    global players
    global current_player
    are_you_sure = input("Are you sure you want to delete your account?\nType yes or no:")
    if are_you_sure == "yes":
        del players[current_player]
        file = open(FILE_NAME, "w")
        json.dump(players, file, indent=4)
        file.close()
        return
    if  are_you_sure == "no":
        return
def change_profile():
    global players
    global current_player
    while True:
        value = input("What would you like to change? Please type one of the following:\nPassword\nGender").capitalize()
        while value not in ["Password", "Gender"]:
            print("Invalid input. Please try again.")
            continue
        new_value = input("What would you like to change it to?: ").capitalize()
        change_profile_specific(value, new_value)
        break

def change_profile_specific(value, new_value):
    global players
    global current_player
    players[current_player][value] = new_value
    file = open(FILE_NAME, "w")
    json.dump(players, file, indent=4)
    file.close()

def show_all_accounts():
    global players
    print(f"""De volgende accounts zijn geregistreerd:""")
    for accounts in players:
        print(accounts)

def save_new_character(new_char_name, new_char_dict):
    global current_player
    global players
    if current_player is None:
        return

    if "Characters" not in players[current_player]:
        players[current_player]["Characters"] = {}

    players[current_player]["Characters"].update({new_char_name: new_char_dict})
    file = open(FILE_NAME, "w")
    json.dump(players, file, indent=4)
    file.close()

def show_account_menu():
    global players
    load_players()
    initialize_player()
    while True:
        print("1. Show all accounts \n2. Create account \n3. Change account \n4. Delete account \n0. Back to main menu")
        account_menu_choice = int(input("Please choose an option"))
        match account_menu_choice:
            case 1:
                show_all_accounts()
                continue
            case 2:
                create_account(username=None)
                continue
            case 3:
                change_profile()
            case 4:
                delete_account()
                continue
            case 0:
                return


