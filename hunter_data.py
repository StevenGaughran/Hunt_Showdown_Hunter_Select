import json
import random

"""The data pulled from 'hunter_list.json', and manipulated into useable form.
Hunter_list pulls the json data.
Owned_hunters searches the json data for True values.
Unowned_hunters searches the json data for False values."""
def hunter_list():
    with open("hunter_list.json", "r") as i:
        hunters = json.load(i)
    return hunters

def owned_hunters(list):
    owned = [k for k, v in list.items() if v == True]
    return owned

def unowned_hunters(list):
    unowned = [k for k, v in list.items() if v == False]
    return unowned

"""Gets the index numbers from the checkboxes.
To be used in ugly_child(checkbox_selection)."""
def get_numbers(numbers):
    for i in numbers:
        numbers = []
        x = i.get()
        return numbers

"""Gets the names necessary for random selection.
Takes the two lists and compares values. 
Exports string with hunter names. 
For example, checkbox_selection is a list of integers pulled from the selected checkboxes.
Hunter_list is pulled from keys from hd.hunter_data.
It is going to return a list of strings."""
def ugly_child(checkbox_selection=None, hunter_list=None):
    chosen_ones = []
    # Find the location of all 1 in checkbox_selection
    for index, element in enumerate(checkbox_selection):
        if element == 1:
    # Find the location of i in the hunter_list
            chosen_ones.append(hunter_list[index])
    return chosen_ones

"""Randomly selects from the ugly_child function.
Hunter_list comes from ugly_child.
Ouput will be a randomly selected string from hunter_list."""
def the_selection(hunter_list=None):
    return random.choice(hunter_list)

"""Determines ownership of hunters.
Compares checkbox-selected hunters against the master list in 'hunter_list.json'.
Switches values in the dictionary from False to True."""
def update_hunter_list(big_hunter_list, chosen_ones):
    updated_hunter_list = big_hunter_list
    for i in chosen_ones:
        if i in updated_hunter_list:
            updated_hunter_list[i] = True
        else:
            updated_hunter_list[i] = False
    return updated_hunter_list

"""Updates the json database of hunters based on user input.
Should I call the json fresh? Or use the 'hunter_list' function defined above?
I'm going to have to call the json data again in any case..."""
def update_json(old_data=None, new_data=None):
    with open('hunter_list.json', 'w') as file:
        data = json.load(file)
        for i in data:
            if i in new_data:
                pass
        pass

"""The goal is to update the .json data using the data from hunter_list"""
def update_json(hunter_list=None):
    pass
    return ["Jan", "Casey"]
