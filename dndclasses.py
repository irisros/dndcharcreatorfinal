import requests

from helper import get_endpoint_data_basic, invalid, format_list

def get_class_proficiency_list(class_choice):
    data = get_endpoint_data_basic(f"https://www.dnd5eapi.co/api/2024/classes/{class_choice}")
    proficiency_data = data["proficiency_choices"][0]["from"]["options"]
    proficiency_list = []
    for proficiency in proficiency_data:
        proficiency_list.append(proficiency["item"]["name"].replace("Skill: ", ""))
    return proficiency_list

def get_class_proficiencies_choices(class_choice):
    proficiency_amount = get_class_proficiency_amount(class_choice)
    proficiency_choice_list = []
    proficiency_list = get_class_proficiency_list(class_choice)
    while proficiency_amount > 0:
        print_formatted_class_proficiencies(proficiency_list)
        proficiency_choice = input("Please choose a proficiency: ").capitalize()
        if proficiency_choice not in proficiency_list:
            invalid()
            continue
        proficiency_amount -= 1
        proficiency_choice_list.append(proficiency_choice)
        while proficiency_amount >= 1:
            print(f"You have {proficiency_amount} choice(s) left.")
            break
        proficiency_list.remove(proficiency_choice)
        continue
    return proficiency_choice_list

def get_class_proficiency_amount(class_type):
    data = get_endpoint_data_basic(f"https://www.dnd5eapi.co/api/2024/classes/{class_type}")
    proficiency_data = data["proficiency_choices"][0]["desc"]
    words = proficiency_data.split()
    return int(words[1][0])

def print_formatted_class_proficiencies(proficiency_list):
    for proficiencies in proficiency_list:
        print(proficiencies)

def class_proficiencies_main(class_choice):
    proficiency_amount = get_class_proficiency_amount(class_choice)
    print(f"These are the proficiency options based on your {class_choice} class. You can choose a total of {proficiency_amount} proficiencies.")
    proficiency_choice_list = get_class_proficiencies_choices(class_choice)
    class_proficiency_choice = format_list(proficiency_choice_list, "and")
    print(f"You have chosen the following proficiencies: {class_proficiency_choice}.")
    return class_proficiency_choice