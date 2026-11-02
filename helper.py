import requests

def invalid():
    print("Invalid choice. Please try again.")

def format_list(items, and_or):
    items = [str(item) for item in items]
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} {and_or} {items[1]}"
    else:
        return ", ".join(items[:-1]) + f" {and_or} " + items[-1]

def print_list_formatted(list):
    for items in list:
        print(items)

def get_endpoint_data_basic(url):
    response = requests.get(url)
    data = response.json()
    return data

def get_endpoint_data_list(url, params=""):
    response = requests.get(url, params=params)
    data = response.json()
    choices_list = []
    for things in data["results"]:
        choices_list.append(things["name"])
    return choices_list

def get_choice(types):
    print_endpoint_formatted(f"https://www.dnd5eapi.co/api/2024/{types}")
    while True:
        choice = input(f"Please choose from the following {types}")
        if choice not in get_endpoint_data_list(f"https://www.dnd5eapi.co/api/2024/{types}"):
            invalid()
            continue
        break
    return choice

def print_endpoint_formatted(url, params=""):
    choices_list = get_endpoint_data_list(url, params="")
    for things in choices_list:
        print(things)

