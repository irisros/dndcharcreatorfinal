from util.helper import get_endpoint_data_basic, print_endpoint_formatted, get_endpoint_data_list

def select_class_or_species_choice(types):
    """
    Prompts the user to select a class or species from the available options.
    :param types: The type of choice (class or species).
    :return: The selected class or species.
    """
    print_endpoint_formatted(f"https://www.dnd5eapi.co/api/2024/{types}")
    while True:
        choice = input(f"Please choose from the following {types}: ").lower()
        if choice not in get_endpoint_data_list(f"https://www.dnd5eapi.co/api/2024/{types}"):
            print("Invalid choice. Please try again.")
            continue
        break
    return choice

def get_class_proficiency_list(class_choice):
    """
    Retrieves the available skill proficiencies for a selected class.

    :param class_choice: The selected character class.
    :return: A list of available skill proficiencies.
    """
    data = get_endpoint_data_basic(f"https://www.dnd5eapi.co/api/2024/classes/{class_choice}")
    proficiency_data = data["proficiency_choices"][0]["from"]["options"]
    proficiency_list = []
    for proficiency in proficiency_data:
        proficiency_list.append(proficiency["item"]["name"].replace("Skill: ", ""))
    proficiency_list = [item.lower() for item in proficiency_list]
    return proficiency_list

def get_class_proficiency_amount(class_type):
    """
    Retrieves the number of proficiencies a character can choose for a class.

    :param class_type: The selected character class.
    :return: The number of proficiencies the user can select.
    """
    data = get_endpoint_data_basic(f"https://www.dnd5eapi.co/api/2024/classes/{class_type}")
    proficiency_data = data["proficiency_choices"][0]["desc"]
    words = proficiency_data.split()
    return int(words[1][0])

def get_class_proficiencies_choices(class_choice):
    """
    Allows the user to select the required number of class proficiencies.

    :param class_choice: The selected character class.
    :return: A list of selected proficiencies.
    """
    proficiency_amount = get_class_proficiency_amount(class_choice)
    proficiency_choice_list = []
    proficiency_list = get_class_proficiency_list(class_choice)
    while proficiency_amount > 0:
        print_formatted_class_proficiencies(proficiency_list)
        proficiency_choice = input("Please choose a proficiency: ").lower()
        if proficiency_choice not in proficiency_list:
            print("Invalid choice. Please try again.")
            continue
        if proficiency_choice in proficiency_choice_list:
            print("You already have this proficiency. Please choose another one.")
            continue

        proficiency_amount -= 1
        proficiency_choice_list.append(proficiency_choice)
        while proficiency_amount >= 1:
            print(f"You have {proficiency_amount} choice(s) left.")
            break
        proficiency_list.remove(proficiency_choice)
        continue
    return proficiency_choice_list

def print_formatted_class_proficiencies(proficiency_list):
    """
    Prints the available class proficiencies with capitalized names.

    :param proficiency_list: A list of available proficiencies.
    """
    proficiency_list = [proficiency.capitalize() for proficiency in proficiency_list]
    for proficiencies in proficiency_list:
        print(proficiencies)

def select_class_proficiencies(class_choice):
    """
    Allows the user to select class proficiencies based on their chosen class.

    :param class_choice: The selected character class.
    :return: A list of selected proficiencies.
    """
    proficiency_amount = get_class_proficiency_amount(class_choice)
    print(f"These are the proficiency options based on your {class_choice} class. You can choose a total of {proficiency_amount} proficiencies.")
    proficiency_choice_list = get_class_proficiencies_choices(class_choice)
    return proficiency_choice_list