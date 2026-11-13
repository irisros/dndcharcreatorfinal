import logging

from util import session, helper

def get_character_list():
    """
    Retrieves the names of all characters belonging to the current user.

    :return: A list containing the names of the user's characters.
    """
    characters = []

    for character in session.users[session.current_user]["Characters"]:
        characters.append(character)

    return characters

def display_character_from_account(character_choice):
    """
    Displays the details of a character selected by the user.

    :param character_choice: The name of the character selected by the user.
    """
    character = session.users[session.current_user]["Characters"][character_choice]

    print(f"Name: {character_choice}")
    print(f"Class: {character['Class'].title()}")
    print(f"Species: {character['Species'].title()}")
    print(f"Proficiencies: {helper.format_list(character['Proficiencies'], 'and').title().replace('And', 'and')}")
    print(f"Background: {character['Background'].title()}")
    print(f"Abilities: {helper.format_dict(character['Abilities'])}")

def display_character_without_login(name_choice, class_choice, proficiencies_choice, species_choice, background_choice, ability_scores):
    """
    Displays the details of a character without requiring the user to be logged in.
    This is specifically for when the user chose to create a character without wanting it saved in their account.

    :param name_choice: The name chosen for the character.
    :param class_choice: The class chosen for the character.
    :param proficiencies_choice: A list containing the character's proficiencies.
    :param species_choice: The species chosen for the character.
    :param background_choice: The background chosen for the character.
    :param ability_scores: A dictionary containing the character's ability scores.
    """
    helper.print_menu_header(name_choice)
    print(f"Name: {name_choice}")
    print(f"Class: {class_choice.title()}")
    print(f"Species: {species_choice.title()}")
    print(f"Proficiencies: {helper.format_list(proficiencies_choice, "and").title().replace("And", "and")}")
    print(f"Background: {background_choice.title()}")
    print(f"Abilities: {helper.format_dict(ability_scores)}")


def select_character():
    """
    Allows the user to select and view one of their saved characters.
    The user can return to the main menu or select another character.
    """
    characters = session.users[session.current_user]["Characters"]

    if not characters:
        logging.warning("User tried to view characters, but does not have any.")
        print("You have no characters yet. Start making one in the character creator!")
        return

    while True:
        character_list = get_character_list()

        print("Your characters:")
        for character in character_list:
            print(character)

        character_choice = input("Who would you like to view?: ")

        if character_choice not in character_list:
            logging.warning("User tried to view a character that they haven't made.")
            print("That character does not exist. Please try again.")
            continue

        helper.print_menu_header(character_choice)
        display_character_from_account(character_choice)

        while True:
            menu_choice = input("Would you like to view anyone else, or go back to the main menu?\n1. Go back to main menu\n2. Select another character\nChoose 1 or 2: "
            ).strip()
            if menu_choice == "1":
                return
            elif menu_choice == "2":
                break
            else:
                print("Invalid. Please try again.")
                continue




