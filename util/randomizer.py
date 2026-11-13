import random

from dnd_name_generator import generate
from util import helper
from dnd_game_mechanics.dnd_classes import get_class_proficiency_list, get_class_proficiency_amount
from dnd_game_mechanics.dnd_backgrounds import get_background_names

def generate_character_name():
    """
    Uses the dnd_name_generator package and generates a name in fantasy style.
    :return: A random name in fantasy style.
    """
    name = generate()
    return name

def randomize_class():
    """
    Uses a function to get data from the 'classes' endpoint in list format, then chooses a
    random class from that list with the random package.
    :return: A random class from the list.
    """
    classes = helper.get_endpoint_data_list(f"https://www.dnd5eapi.co/api/2024/classes")
    random_class = random.choice(classes)
    return random_class

def randomize_class_proficiencies(class_choice):
    """
    Retrieves the list of available proficiencies for a given class, as well as the number
    of proficiency choices that the class allows. It then uses the random package to randomly
    select the specified number of proficiencies from the available list.
    :param: class_choice
    :return: a list of random proficiencies based on choice of class.
    """
    class_proficiencies_list = get_class_proficiency_list(class_choice)
    class_proficiency_amount = get_class_proficiency_amount(class_choice)
    random_class_proficiencies = random.sample(class_proficiencies_list, class_proficiency_amount)
    return random_class_proficiencies

def randomize_species():
    """
    ses a function to get data from the 'species' endpoint in list format, then chooses a
    random class from that list with the random package.
    :return:
    """
    species = helper.get_endpoint_data_list(f"https://www.dnd5eapi.co/api/2024/species")
    random_species = random.choice(species)
    return random_species

def randomize_ability_scores():
    """
    Randomly assigns a number to an ability, and puts these scores together in a dictionary.
    :return: The dictionary of randomized ability scores.
    """
    ability_scores_available = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    numbers_available = [15, 14, 13, 12, 10, 8]

    random.shuffle(ability_scores_available)
    random.shuffle(numbers_available)

    return dict(zip(ability_scores_available, numbers_available))

def randomize_background():
    """
    Uses a function to get all available background names in a list, then chooses a
    random background from that list with the random package.
    :return: A random background.
    """
    backgrounds = get_background_names()
    random_background = random.choice(backgrounds)
    return random_background