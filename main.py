import logging
import sys

from menus.profiles import run_account_menu
from menus.character_creator import character_creator_select
from util.helper import print_menu_header, print_menu_line

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def show_main_menu():
    """
    Shows the main menu of the application, including the different menu options.
    """
    print_menu_header("Main Menu")
    print("Welcome! This is an application that you can use to customize \nand save your self-created D&D inspired characters.")
    print("")
    print("1. Show character creator menu \n2. Show account menu \n3. Exit application")
    print_menu_line()

def main():
    """
    Starts the application and takes care of the navigation between the character creation menu
    and the account menu, based on the input of the user.
    """
    logging.info("Application started")
    while True:
        show_main_menu()

        while True:
            try:
                main_menu_choice = int(input("Please choose option 1, 2 or 3: "))
                logging.info(f"User chose main menu option {main_menu_choice}")

                match main_menu_choice:
                    case 1:
                        logging.info("Character creator menu opened")
                        character_creator_select()
                        break
                    case 2:
                        logging.info("Account menu opened")
                        run_account_menu()
                        break
                    case 3:
                        print("Thank you for using this application. See you next time!")
                        sys.exit(1)
                    case _:
                        logging.warning("User entered invalid number")
                        print("Invalid number. Please choose option 1 or 2")

            except ValueError:
                logging.warning("User entered invalid input")
                print("Invalid input. Please enter a number!")


if __name__ == '__main__':
    main()
