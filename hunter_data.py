import json
import random

"""The data pulled from 'hunter_list.json', and manipulated into useable form."""
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