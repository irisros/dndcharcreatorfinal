import logging

from dnd_game_mechanics.dnd_classes import select_class_or_species_choice

from menus.profiles import login_or_create_account, load_users_from_file, save_player_character
from menus.view_character import select_character, display_character_from_account, display_character_without_login

from dnd_game_mechanics.dnd_classes import select_class_proficiencies
from dnd_game_mechanics.dnd_abilityscores import select_ability_scores, apply_ability_bonus, get_full_ability_score_name
from dnd_game_mechanics.dnd_backgrounds import select_background, get_background_ability_scores, get_background_proficiencies

from util import session, randomizer, helper

def show_character_creator_menu():
    """
     Displays the character creator menu and its available options.
    """
    helper.print_menu_header("Character Creator Menu")
    print("Welcome to the character creator.")
    print("")
    print("1. Make a new character from scratch \n2. Generate a random character \n3. View characters \n4. Go back to the main menu")

def prompt_login():
    """
    Checks whether the user is logged in and, if not, asks whether they would like to log in
    to be able to save their created characters.
    If the user chooses to log in, the user data is loaded and the account menu is started.
    """
    if session.current_user is None:
        print("If you would like to save the character you will make,\nyou need to login. Would you like to?")
        while True:
            login_choice = input("Please type yes or no: ").lower()
            if login_choice == "yes":
                logging.info("User continues logged in.")
                load_users_from_file()
                login_or_create_account()
                break
            elif login_choice == "no":
                logging.info("User continues without account.")
                print("Continuing without account.")
                break
            else:
                print("Invalid input. Please try again.")

def character_creator_select():
    """
    Takes care of the entire character creation process and allows the user to choose
    between creating a character from scratch, generating a random character
    or viewing existing characters.

    Making a character from scratch: Prompts the user to select character attributes, including name, class,
    proficiencies, species, ability scores and background. Saves the character to the user's account.

    generating a random character: generates a random character and then saves it to the user's account.

    viewing existing characters: forces the user to login before the user can make use of the character viewer.
    """
    prompt_login()
    show_character_creator_menu()
    while True:
        try:
            character_menu_choice = int(input("Please choose either 1, 2, 3 or 4: "))
            match character_menu_choice:
                case 1:
                    logging.info("User chose to create a character from scratch.")

                    helper.print_menu_header("Customize Character: Name")
                    name_choice = input("What would you like to call your character? If you want a random name, type 'random'\nType your choice here: ").lower()
                    if name_choice == "random":
                        name_choice = randomizer.generate_character_name()
                    print(f"Character name is {name_choice}.")

                    helper.print_menu_header("Customize Character: Class")
                    class_choice = int(input("Would you like to choose your class or randomize it?\n1. Choose\n2. Randomize\nChoose here: "))
                    if class_choice == 1:
                        class_choice = select_class_or_species_choice("classes")
                    elif class_choice == 2:
                        class_choice = randomizer.randomize_class()
                    print(f"Your character's class is {class_choice.capitalize()}.")

                    helper.print_menu_header("Customize Character: Class Proficiencies")
                    class_proficiency_choice = int(input("Would you like to choose your class proficiencies or randomize them?\n1. Choose\n2. Randomize\nChoose here: "))
                    if class_proficiency_choice == 1:
                        class_proficiency_choice = select_class_proficiencies(class_choice)
                    elif class_proficiency_choice == 2:
                        class_proficiency_choice = randomizer.randomize_class_proficiencies(class_choice)
                    print(f"Your class proficiency choices are {helper.format_list(class_proficiency_choice, "and").capitalize().replace("And", "and")}.")

                    helper.print_menu_header("Customize Character: Species")
                    species_choice = int(input("Would you like to choose your species or randomize it?\n1. Choose\n2. Randomize\nChoose here: "))
                    if species_choice == 1:
                        species_choice = select_class_or_species_choice("species")
                    elif species_choice == 2:
                        species_choice = randomizer.randomize_species()
                    print(f"Your character is a(n) {species_choice.capitalize()}.")

                    helper.print_menu_header("Customize Character: Ability Scores")
                    abilities_choice = int(input("Would you like to choose your ability scores or randomize them?\n1. Choose\n2. Randomize\nChoose here: "))
                    if abilities_choice == 1:
                        abilities_choice = select_ability_scores(class_choice)
                    elif abilities_choice == 2:
                        abilities_choice = randomizer.randomize_ability_scores()

                    helper.print_menu_header("Customize Character: Background")
                    background_choice = int(input("Would you like to choose your backstory or randomize it?\n1. Choose\n2. Randomize\nChoose here: "))
                    if background_choice == 1:
                        background_choice = select_background()
                    elif background_choice == 2:
                        background_choice = randomizer.randomize_background()
                    background_proficiency_choice = get_background_proficiencies(background_choice)
                    background_ability_scores_choice = get_background_ability_scores(background_choice)
                    abilities_full_names = get_full_ability_score_name(background_ability_scores_choice)

                    print(f"Your character's background is {background_choice}. Their {helper.format_list(abilities_full_names,"and")} increased by 1.")

                    proficiencies_choice = background_proficiency_choice + class_proficiency_choice

                    proficiencies_choice = list(set(proficiencies_choice))

                    ability_scores = apply_ability_bonus(abilities_choice, background_ability_scores_choice)

                    if session.current_user is None:
                        display_character_without_login(name_choice, class_choice, proficiencies_choice, species_choice, background_choice, ability_scores)

                        input("Type anything to return to the main menu...")
                        logging.info("User returned to the main menu.")
                        return

                    else:
                        new_char_dict = {"Class" : class_choice,
                                         "Proficiencies" : proficiencies_choice,
                                         "Species" : species_choice,
                                         "Background" : background_choice,
                                         "Abilities" : ability_scores}

                        save_player_character(name_choice, new_char_dict)

                        logging.info(f"The user's created character with name {name_choice} was saved.")
                        helper.print_menu_header(f"Character {name_choice} Saved!")

                        display_character_from_account(name_choice)

                        input("Type anything to return to the main menu...")
                        logging.info("User returned to the main menu.")
                        return

                case 2:
                    logging.info("User chose to generate a random character.")

                    print("Generating a random character...")

                    name_choice = randomizer.generate_character_name()
                    class_choice = randomizer.randomize_class()
                    class_proficiency_choice = randomizer.randomize_class_proficiencies(class_choice)
                    species_choice = randomizer.randomize_species()
                    background_choice = background_choice = randomizer.randomize_background()
                    abilities_choice = abilities_choice = randomizer.randomize_ability_scores()
                    background_proficiency_choice = get_background_proficiencies(background_choice)

                    proficiencies_choice = background_proficiency_choice + class_proficiency_choice
                    proficiencies_choice = list(set(proficiencies_choice))

                    background_ability_scores_choice = get_background_ability_scores(background_choice)
                    ability_scores = apply_ability_bonus(abilities_choice, background_ability_scores_choice)

                    if session.current_user is None:

                        display_character_without_login(name_choice, class_choice, proficiencies_choice, species_choice, background_choice, ability_scores)

                        input("Type anything to return to the main menu...")
                        logging.info("User returned to the main menu.")
                        return


                    else:
                        new_char_dict = {"Class": class_choice,
                                         "Proficiencies": proficiencies_choice,
                                         "Species": species_choice,
                                         "Background": background_choice,
                                         "Abilities": ability_scores}

                        save_player_character(name_choice, new_char_dict)
                        helper.print_menu_header(f"Character {name_choice} Saved!")
                        display_character_from_account(name_choice)

                        input("Type anything to return to the main menu...")
                        logging.info("User returned to the main menu.")
                        return


                case 3:
                    logging.info("User chose to view their created character(s)")

                    if session.current_user is None:
                        logging.info("User is not logged in so can't view saved characters.")
                        print("Please log in before viewing your characters.")
                        load_users_from_file()
                        login_or_create_account()
                    else:
                        select_character()

                case 4:
                    logging.info("User returned to main menu.")
                    return

                case _:
                    logging.warning("User entered invalid number.")
                    print("Invalid number. Please choose option 1, 2, 3 or 4.")

        except ValueError:
            logging.warning("User entered invalid input")
            print("Invalid input. Please enter a number!")





















