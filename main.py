import requests
from profiles import show_account_menu
from charactercreator import character_creator_main

def show_main_menu():
    menu_choice = int(input("1. Create new character \n2. Show account menu \nPlease choose option 1 or 2: "))
    return menu_choice

def main():
    print("Welcome! This is an application that you can use to customize and save your self-created DND inspired characters.")
    while True:
        main_menu_choice = show_main_menu()
        match main_menu_choice:
            case 1:
                character_creator_main()
            case 2:
                show_account_menu()
                continue
            case _:
                print("Invalid choice. Please try again.")
                continue

if __name__ == '__main__':
    main()
