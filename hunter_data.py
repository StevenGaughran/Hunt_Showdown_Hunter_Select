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

# A list of owned hunters, based on True key values in 'hunter_list.json'
def owned_hunters(list):
    owned = [k for k, v in list.items() if v == True]
    return owned

# A list of unowned hunters, based on False key values in 'hunter_list.json'
def unowned_hunters(list):
    unowned = [k for k, v in list.items() if v == False]
    return unowned

"""Gets the index numbers from the checkboxes.
To be used in ugly_child(checkbox_selection).
Currently, problematic. It creates a whole BUNCH of lists, rather than one list with integers."""
def get_numbers(numbers):
    for i in numbers:
        number_list = []
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

"""The OLD button that runs the function that randomly selects your Hunter.
Will likely need to rewrite this from scratch."""
def the_button():
#     # list_numbers = hunter_list.curselection()
#     # # This writes the index locations of selected numbers to a Word file, for future list pre-generation.
#     # with open ("hunter_list_index.txt", "w") as edit:
#     #     edit.truncate(0)
#     #     edit.write(str(list_numbers))
#     #
#     # # This gives you your randomly selected hunter.
#     # selection_list = []
#     # for i in list_numbers:
#     #     y = hunter_list.get(first=i)
#     #     selection_list.append(y)
#     # selection_prompt.config(text=random.choice(selection_list))
    pass

"""Updates the json database of hunters based on user input.
Replaces the dictionary in 'hunter_list.json' with that from 'update_hunter_list' function'
"""
def update_json(new_data=None):
    with open('hunter_list.json', 'w') as file:
        data = json.load(file)
        pass
