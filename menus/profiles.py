import json
import logging

from util import session, helper

FILE_NAME = "data/users.json"

def load_users_from_file():
    """
    Loads user data from "users.json" into a dictionary called "users".
    """
    file = open(FILE_NAME, "r")
    session.users = json.load(file)
    file.close()

def login_or_create_account():
    """
    Prompts the user to enter a username.

    If their input is empty, starts over from the beginning of the function.

    If the username already exists, the user is asked to verify
    their password and is logged in.

    If the username does not exist, a new account is created.

    """
    username = input("What is your username?: ").strip()
    while True:
        if not username:
            logging.warning("User entered an empty username")
            print("Username can't be empty!")
            continue

        if username in session.users:
            verify_password(username)
            session.current_user = username
            logging.info(f"User is logged in as {session.current_user}")
            helper.print_menu_header(f"Logged in as {session.current_user}")
            return

        else:
            logging.info("New account creation started")
            print("No existing account found. Creating a new account.")
            create_account(username)
            session.current_user = username
            helper.print_menu_header(f"Account with name {session.current_user} was created!")
            return

def verify_password(username):
    """
    Prompts the user to enter their password.

    Checks if the password is correct by comparing the password check to the password that is stored in users.json.
    """
    password = session.users[username]["Password"]

    while True:
        password_check = input("Please enter your password: ")
        if password == password_check:
            logging.info("Password verified successfully.")
            return

        if password != password_check:
            logging.warning("User filled in the wrong password.")
            print("Wrong password. Try again.")
            continue


def create_account(username=None):
    """
    Creates a new user account. Checks whether the username the user wants to use already exists.

    Prompts the user to create a new password.

    :param username: Optional username. If provided, it is used
                     instead of asking the user to enter one.
    """
    if username is None:
        username = input("What is your username?: ").strip()
        if not username:
            logging.warning("User attempted to create an account with an empty username.")
            print("Username cannot be empty!")
        if username in session.users:
            logging.warning("User tried to create an account with an existing username.")
            print("This account already exists. Please log into your existing account, or choose another name.")
            return

    while True:
        password = input("Create a new password: ")
        check_password = input("Please repeat your password: ")
        if check_password == password:
            session.users[username] = {
                "Password": password,
                "Characters": {},
            }
            safe_users_to_file()

            logging.info("Password was created and account was saved.")
            print("Password created.")
            break
        else:
            logging.warning("Password confirmation did not match.")
            print("Please try again")
            continue

def safe_users_to_file():
    """
    Saves the user data from session.users to users.json.
    """
    file = open(FILE_NAME, "w")
    json.dump(session.users, file, indent=4)
    file.close()

    logging.info("Successfully saved information to users.json ")


def delete_account():
    while True:
        are_you_sure = input("Are you sure you want to delete your account?\nType yes or no:").lower().strip()
        if are_you_sure == "yes":
            del session.users[session.current_user]
            session.current_user = None
            safe_users_to_file()
            logging.info("Account successfully deleted")
            print("Account successfully deleted")
            return
        elif are_you_sure == "no":
            logging.info("Account deletion canceled")
            print("Account deletion canceled.")
            return
        else:
            print("Invalid input. Please type yes or no.")
            continue

def change_password():
    while True:
        new_password = input("What would you like to change your password to?: ")
        if not new_password:
            logging.warning("User tried to fill in an empty password.")
            print("Password can't be empty!")
            return
        else:
            session.users[session.current_user]["Password"] = new_password
            safe_users_to_file()
            print("New password was created and saved.")
            logging.info("New password was created and saved.")
            break

def display_all_accounts():
    if not session.users:
        print("There are no users registered yet.")
    else:
        print("The following accounts are registered:")
        for accounts in session.users:
            print(accounts)

def save_player_character(name_choice, choices_dict):
    """
    Saves a character to the users.json file. If the user
    chose to not log in and not save their character, the function will not do anything.
    :param name_choice: The name chosen by the user for the character
    :param choices_dict:  A dictionary containing all the character's choices.
    """
    if session.current_user is None:
        return
    session.users[session.current_user]["Characters"].update({name_choice: choices_dict})
    logging.info("Character was saved!")

    safe_users_to_file()

def run_account_menu():
    """
    First loads all users from the users.json file, then prompts the user to log in.
    Then lets the user navigate through the account menu. The user can choose to either display all accounts,
    change their password, delete their account, or return to the main menu.
    """
    helper.print_menu_header("Account Menu")

    if session.current_user is None:
        load_users_from_file()
        login_or_create_account()

    while True:
        try:
            print("1. Show all accounts \n2. Change password \n3. Delete account \n4. Back to main menu")
            account_menu_choice = int(input("Please choose option 1, 2, 3 or 4: "))
            match account_menu_choice:
                case 1:
                    logging.info("User prompted to see all registered accounts.")
                    display_all_accounts()
                    continue
                case 2:
                    logging.info("User initiated a password change.")
                    change_password()
                    continue
                case 3:
                    logging.info("User initiated an account deletion.")
                    delete_account()
                case 4:
                    logging.info("User returned to main menu.")
                    return
                case _:
                    logging.warning("User entered an invalid number")
                    print("Invalid number. Please choose option 1, 2, 3 or 4.")
        except ValueError:
            logging.warning("User entered invalid input")
            print("Invalid input. Please enter a number!")


