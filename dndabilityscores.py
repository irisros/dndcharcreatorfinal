from helper import format_list, invalid, get_endpoint_data_basic

def get_primary_ability(class_choice):
    data = get_endpoint_data_basic(f"https://www.dnd5eapi.co/api/2024/classes/{class_choice}")
    primary_ability = data["primary_ability"]["desc"]
    return primary_ability

def ability_scores_main(class_choice):
    print("This character creator determines ability scores according to the Standard array of 15, 14, 13, 12, 10, 8. This means that ...")
    print(f"Based on your class choice ({class_choice}), it is recommended to choose the highest score for your primary ability, which is {get_primary_ability(class_choice)}.")
    while True:
        ability_scores = {}
        numbers_available = [15, 14, 13, 12, 10, 8]

        ability_scores_available = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        while len(numbers_available) > 1:
            score_choice = int(input(f"What would you like to assign to {ability_scores_available[0]}? Please type {format_list(numbers_available, "or")}: "))
            if score_choice not in numbers_available:
                invalid()
                continue
            ability_scores.update({ability_scores_available[0] : score_choice})
            numbers_available.remove(score_choice)
            ability_scores_available.remove(ability_scores_available[0])

        print(f"{numbers_available[0]} was assigned to {ability_scores_available[0]}")
        ability_scores.update({ability_scores_available[0] : numbers_available[0]})


        return ability_scores

ability_scores_main("druid")