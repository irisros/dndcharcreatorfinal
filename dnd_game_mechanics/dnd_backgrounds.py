from util.helper import get_endpoint_data_basic, format_list

import json

FILE_NAME = "data/background-information.json"

def load_background_information():
    """
    Loads background information from a JSON file.
    :return: A dictionary containing background information.
    """
    background_file = open(FILE_NAME, "r")
    backgrounds = json.load(background_file)
    background_file.close()

    return backgrounds

def get_background_ability_scores(background):
    """
    Retrieves the ability score bonuses associated with a character
    background from the background endpoint. Extracts the ability score,
    converts them to lowercase and stores them in a list.

    :param background: The character background.
    :return: A list containing the bonus ability scores.
    """
    bonuses = []
    data = get_endpoint_data_basic(f"https://www.dnd5eapi.co/api/2024/backgrounds/{background}")
    for item in data["ability_scores"]:
        bonuses.append(item["index"].lower())

    return bonuses

def get_background_proficiencies(background):
    """
    Retrieves the skill proficiencies associated with a background.
    Deletes Tool proficiencies, as these are outside the scope of this application.

    :param background: The character background.
    :return: A list of skill proficiencies.
    """
    proficiencies = []
    data = get_endpoint_data_basic(f"https://www.dnd5eapi.co/api/2024/backgrounds/{background}")
    for item in data["proficiencies"]:
        if "Tool" in item["name"]:
            continue
        proficiencies.append(item["name"].replace("Skill: ", "").lower())

    return proficiencies

def get_background_names():
    """
    Retrieves the names of all available backgrounds.

    :return: A list containing the background names.
    """
    data = get_endpoint_data_basic("https://www.dnd5eapi.co/api/2024/backgrounds")
    backgrounds = []
    for items in data["results"]:
        backgrounds.append(items["index"].lower())
    return backgrounds

def get_background_information(background):
    """
    Retrieves information about a specific background from the JSON file.
    I made this JSON file with additional information about the backgrounds, based on the
    official D&D wiki.

    :param background: The selected background.
    :return: A dictionary containing the background information.
    """
    all_backgrounds = load_background_information()
    specific_background_information = all_backgrounds[background]
    return specific_background_information

def select_background():
    """
    Prompts the user to select a character background from the available
    backgrounds retrieved from the background endpoint. to request additional information about
    a specific background by typing 'information' followed by the background
    name. If a valid background is selected, it is returned. If the input is invalid, the user
    needs to try again.

    :return: The name of the selected character background.
    """
    backgrounds = get_background_names()
    formatted_backgrounds = format_list(backgrounds, "or")
    print("Please type your choice of background. If you want more information about the background, please type the word 'information' in front of the background.")
    while True:
        print(f"The following backgrounds are available: {formatted_backgrounds}.")
        choice = input("Type your answer here: ").lower()
        while True:
            if "information" in choice:
                choice_list = choice.split(" ")
                print(get_background_information(choice_list[1]))
                break
            elif choice in backgrounds:
                return choice
            else:
                print("Invalid choice. Please try again.")