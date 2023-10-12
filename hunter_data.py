import json
import random
from tkinter import Tk,Label,scrolledtext,Button,IntVar,Checkbutton

"""The data pulled from 'hunter_list.json', and manipulated into useable form.
Hunter_list pulls the json data.
Owned_hunters searches the json data for True values.
Unowned_hunters searches the json data for False values."""
def hunter_list():
    with open("hunter_list.json", "r") as i:
        hunters = json.load(i)
    return hunters

# A list of owned hunters, based on True key values in 'hunter_list.json'
def owned_hunters(list):
    owned = [k for k, v in list.items() if v == True]
    return owned

# A list of unowned hunters, based on False key values in 'hunter_list.json'
def unowned_hunters(list):
    unowned = [k for k, v in list.items() if v == False]
    return unowned

# Creates a list of Hunter names derived from 'hunter_list'
def hunter_names(big_list):
    h_list = []
    for i in big_list:
        h_list.append(i)
    return h_list

"""This fills in the window with hunter names, and pre-selects them if they are 'owned'.
Populates the hunter_list_numbers with returned IntVars."""
def populate_hunter_list(text=None):
    hunter_list_numbers = []
    for i in hunter_list():
        if i in owned_hunters(hunter_list()):
            var = IntVar()
            cb = Checkbutton(pady=2,
                             text=i,
                             bg='white',
                             anchor='w',
                             variable=var)
            cb.select()
            hunter_list_numbers.append(var)
            text.window_create('end', window=cb)
            text.insert('end', '\n')
        elif i in unowned_hunters(hunter_list()):
            var = IntVar()
            cb = Checkbutton(pady=2,
                             text=i,
                             bg='white',
                             anchor='w',
                             variable=var)
            hunter_list_numbers.append(var)
            text.window_create('end', window=cb)
            text.insert('end', '\n')
    return hunter_list_numbers

"""Gets the index numbers from the checkboxes.
To be used in ugly_child(checkbox_selection)."""
def get_numbers(numbers):
    number_list = []
    for i in numbers:
        x = i.get()
        number_list.append(x)
    return number_list

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
    print(random.choice(hunter_list))

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

"""The function that randomly selects your Hunter from 'ugly_child'."""
def random_hunter_selection(chosen_ones=None, selection_prompt=None):
    selection_prompt.config(text=random.choice(chosen_ones)) #How to actualize this?
    pass

def the_button():
    pass

"""Updates the json database of hunters based on user input.
Replaces the dictionary in 'hunter_list.json' with that from 'update_hunter_list' function'
Can I combine this with 'update_hunter_list' above? Probably!
"""
def update_json(new_data=None):
    with open('hunter_list.json', 'r') as file:
        data = json.load(file)
        pass

"""The button that pulls all this nonsense together."""
def the_button(hunter_list_numbers=None):
    nums = get_numbers(hunter_list_numbers) # Not sure how to use this to make the whole thing work?
    selection = ugly_child(nums, hunter_names(hunter_list()))
    random_hunter_selection(selection)
