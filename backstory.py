from helper import get_endpoint_data_basic, format_list

def get_background_list():
    data = get_endpoint_data_basic("https://www.dnd5eapi.co/api/2024/backgrounds")
    backgrounds = []
    for items in data["results"]:
        backgrounds.append(items["index"])
    return backgrounds

def background_main():
    backgrounds = get_background_list()
    formatted_backgrounds = format_list(backgrounds, "or")


print(get_background_list())