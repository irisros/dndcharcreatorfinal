import requests

def print_menu_header(text):
    """
    Creates a header that contains text in bold.
    :param text: the header text.
    """
    bold = '\033[1m'
    reset = '\033[0m'

    print(60 * "=")
    print(bold + f"{text:^60}" + reset)
    print(60 * "=")

def print_menu_line():
    print(60 * "=")

def format_list(items, and_or):
    """
    Takes a list and formats it in with comma's and an 'and/or' at the end.
    It first makes sure that all items are converted to a string.
    If the list is only 1 item long, it just returns that item.
    If the list is only 2 items long, it returns the two items with 'and/or' in between.
    If the list is longer than two, it will put comma's everywhere but the last two items,
    which has an 'and/or' depending on the parameter given.
    :param items: the list.
    :param and_or: determines whether there is an 'and' or an 'or' between the last two items of the list.
    :return: the formatted list.
    """
    items = [str(item) for item in items]
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} {and_or} {items[1]}"
    else:
        return ", ".join(items[:-1]) + f" {and_or} " + items[-1]

def format_dict(dictionary):
    """
    Formats a dictionary in the following format: 'key = value,'.
    Removes the comma from the last item.
    :param: dictionary.
    :return: the formatted dictionary.
    """
    formatted_string = ""
    for key, value in dictionary.items():
        formatted_string += f"{key} = {value}, "

    return formatted_string.rstrip(", ")

def get_endpoint_data_basic(url):
    """
    Gets data from a specific endpoint, based on the URL that is given in the parameter.
    :param url: URL of endpoint.
    :return: Data in endpoint.
    """
    response = requests.get(url)
    data = response.json()
    return data

def get_endpoint_data_list(url):
    """
    Gets data from a specific endpoint, based on the URL that is given in the parameter,
    and returns it into a list.
    :param url: URL of endpoint.
    :return: List of data in endpoint.
    """
    response = requests.get(url)
    data = response.json()
    choices_list = []
    for things in data["results"]:
        choices_list.append(things["name"])
    choices_list = [item.lower() for item in choices_list]
    return choices_list

def print_endpoint_formatted(url):
    """
    Gets endpoint data through the get_endpoint_data_list function, and prints the items
    in a formatted way (listed one below the other).
    :param url: URL of an endpoint.
    """
    choices_list_formatted = [item.capitalize() for item in get_endpoint_data_list(url)]
    for choices in choices_list_formatted:
        print(choices)
