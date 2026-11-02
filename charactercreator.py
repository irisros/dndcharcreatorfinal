import requests

from helper import print_endpoint_formatted, get_choice
from profiles import initialize_player, load_players, check_if_logged_in, save_new_character
from dndclasses import class_proficiencies_main
from dndabilityscores import ability_scores_main

def want_to_save_character():
    if check_if_logged_in() == True:
        print("If you would like to save the character you will make, you need to login. Would you like to?")
        login_choice = input("Please type yes or no: ")
        if login_choice == "yes":
            load_players()
            initialize_player()
        else:
            print("Continuing without account.")
    else:
        return

def show_character_creator_menu():
    print("Welcome to the character creator.")
    want_to_save_character()
    character_menu_choice = int(input("1. Make a new character from scratch \n2. Generate a random character \nPlease choose either 1 or 2: "))
    return character_menu_choice

def get_class_proficiency_choice(class_type):
    return

def get_species_choice():
    return get_choice("species")



#def get_spells_choice(class_choice):
    class_choice = class_choice.lower()
    print(f"""Based on your class choice ({class_choice}), the following spells are available: """)
    print_endpoint_formatted(f"https://www.dnd5eapi.co/api/2024/classes/{class_choice}/spells")


def character_creator_main():
    while True:
        charactor_menu_choice = show_character_creator_menu()
        match charactor_menu_choice:
            case 1:
                name_choice = input("What would you like to call your character?: ")

                class_choice = get_choice("classes").lower()

                class_proficiency_choice = class_proficiencies_main(class_choice)

                species_choice = get_choice("species")

                abilities_choice = ability_scores_main(class_choice)


                new_char_dict = { "Class" : class_choice, "Proficiencies" : class_proficiency_choice, "Species" : species_choice, "Abilities" : abilities_choice}
                save_new_character(name_choice, new_char_dict)














