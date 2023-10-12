import json
import random
from tkinter import IntVar,Checkbutton

"""The data pulled from 'hunter_list.json', and manipulated into useable form.
Hunter_list pulls the json data.
Owned_hunters searches the json data for True values.
Unowned_hunters searches the json data for False values."""
def hunter_list():
    with open("hunter_list.json", "r") as i:
        hunters = json.load(i)
    return hunters

# A list of owned hunters, based on True key values in 'hunter_list.json'
def owned_hunters(hunter_list=None):
    owned = [k for k, v in hunter_list.items() if v == True]
    return owned

# A list of unowned hunters, based on False key values in 'hunter_list.json'
def unowned_hunters(hunter_list=None):
    unowned = [k for k, v in hunter_list.items() if v == False]
    return unowned

# Creates a list of Hunter names derived from 'hunter_list'
def hunter_names(hunter_list=None):
    h_list = []
    for i in hunter_list:
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
def get_numbers(hunter_list_numbers=None):
    number_list = []
    for i in hunter_list_numbers:
        x = i.get()
        number_list.append(x)
    return number_list

"""Gets the names necessary for random selection.
Takes the two lists and compares values. 
Exports string with hunter names. 
For example, checkbox_selection is a list of integers pulled from the selected checkboxes.
Returns a list of strings."""
def ugly_child(get_numbers=None, hunter_names=None):
    chosen_ones = []
    # Find the location of all 1 in checkbox_selection
    for index, element in enumerate(get_numbers):
        if element == 1:
    # Find the location of i in the hunter_list
            chosen_ones.append(hunter_names[index])
    return chosen_ones

"""The function that randomly selects your Hunter from 'ugly_child'."""
def random_hunter_selection(ugly_child=None):
    selection = random.choice(ugly_child)
    return selection

"""Updates the json database of hunters based on user input.
Checks the output of 'chosen_ones' against the master hunter list.
If the names in 'chosen_ones' are in the master list, makes the appropriate value 'true'.
Otherwise, makes it 'false'."""
def update_json(ugly_child=None):
    with open('hunter_list.json', 'r') as file:
        data = json.load(file)
        for i in data:
            if i in ugly_child:
                data[i] = True
            else:
                data[i] = False
    with open('hunter_list.json', 'w') as f:
        json.dump(data,f)

"""The button that pulls all this nonsense together.
THIS MAY BE PROBLEMATIC. CANNOT CALL A () IN A BUTTON command= LINE
"""
def the_button(hunter_list_numbers=None, selection_prompt=None):
    chosen_ones = ugly_child(
        get_numbers=get_numbers(hunter_list_numbers),
        hunter_names=hunter_names(hunter_list()))
    selection = random_hunter_selection(ugly_child=chosen_ones)
    selection_prompt.config(text=selection)
    update_json(ugly_child=chosen_ones)