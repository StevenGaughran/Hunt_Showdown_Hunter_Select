import json
import random

# The hunter data.
# Use hunter_list()[0] for the base list, hunter_list()[1] for owned/TRUE hunters, or hunter_list()[2] for unowned/FALSE hunters.
def hunter_list():
    with open("hunter_list.json", "r") as i:
        hunters = json.load(i)
        owned = [k for k, v in hunters.items() if v == True]
        not_owned = [k for k, v in hunters.items() if v == False]
    return hunters

# The following two functions are me compensating for the fact that I couldn't figure something out.
# I figured it out, so they are PROBABLY no longer necessary?
# def owned_hunters(list):
#     owned = [k for k, v in list.items() if v == True]
#     return owned
#
# def unowned_hunters(list):
#     unowned = [k for k, v in list.items() if v == False]
#     return unowned

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

"""The goal is to update the .json data using the data from hunter_list"""
def update_json(hunter_list=None):
    pass


    return ["Jan", "Casey"]