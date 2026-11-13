from util.helper import format_list, get_endpoint_data_basic

def get_primary_ability(class_choice):
    """
    Retrieves the primary ability or abilities for a specific class.

    :param class_choice: The class selected by the user.
    :return: The primary ability or abilities, specific to the user's chosen class.
    """
    data = get_endpoint_data_basic(f"https://www.dnd5eapi.co/api/2024/classes/{class_choice}")
    primary_ability = data["primary_ability"]["desc"]
    return primary_ability.lower()

def get_full_ability_score_name(score):
    """
    Converts a three-letter ability score abbreviation into its full name (for example: STR to strength)
    :param score: the three letter ability score.
    :return: the full name of the ability score.
    """
    full_ability_score_names = []
    for item in score:
        data = get_endpoint_data_basic(f"https://www.dnd5eapi.co/api/2024/ability-scores/{item}")
        full_ability_score_names.append(data["full_name".lower()])
    return full_ability_score_names

def apply_ability_bonus(ability_scores, bonus_scores):
    """
    Applies the ability score bonus that is based on background to the chosen/randomized
    base ability scores.
    :param ability_scores: base ability scores.
    :param bonus_scores: scores retrieved from background.
    :return:
    """
    ability_bonus = get_full_ability_score_name(bonus_scores)
    for score in ability_bonus:
        if score in ability_scores:
            ability_scores[score] += 1
    return ability_scores

def select_ability_scores(class_choice):
    """
    Allows the user to manually assign ability scores to their character
    using the standard array (15, 14, 13, 12, 10, 8).

    Displays the recommended primary ability score based on the selected
    character class.

    The user is then prompted to assign each available score to an ability
    of their choice. Once a score has been assigned, it is removed from the
    available scores to prevent duplicate assignments.
    :param: class_choice
    :return: A dictionary with the six ability scores and their assigned values.
    """
    print("This character creator determines ability scores according to the Standard array of 15, 14, 13, 12, 10, 8.\nPlease assign your preferred score to the available abilities.")
    print(f"Based on your class choice ({class_choice}), it is recommended to choose the highest score for your primary ability, which is {get_primary_ability(class_choice)}.")
    while True:
        ability_scores = {}
        numbers_available = [15, 14, 13, 12, 10, 8]

        ability_scores_available = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        while len(numbers_available) > 1:
            try:
                score_choice = int(input(f"What would you like to assign to {ability_scores_available[0]}? Please type {format_list(numbers_available, "or")}: "))
                if score_choice not in numbers_available:
                    print("Invalid. Please input a number from the available scores.")
                    continue

            except ValueError:
                print("Invalid. Please input a number from the available scores.")
                continue

            ability_scores.update({ability_scores_available[0] : score_choice})
            numbers_available.remove(score_choice)
            ability_scores_available.remove(ability_scores_available[0])

        print(f"{numbers_available[0]} was assigned to {ability_scores_available[0]}")
        ability_scores.update({ability_scores_available[0] : numbers_available[0]})


        return ability_scores
