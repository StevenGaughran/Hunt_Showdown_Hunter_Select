import json
import random
from tkinter import IntVar,Checkbutton,Toplevel,Label,Button

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

"""Gets the index numbers from the checkbox IntVars."""
def get_numbers(hunter_list_numbers=None):
    number_list = []
    for i in hunter_list_numbers:
        x = i.get()
        number_list.append(x)
    return number_list

"""Gets the names necessary for random selection.
Takes the two lists and creates an index. 
Uses the index to pull the appropriate names.
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

"""Function to open a new window to place the hunter selected from 'random_hunter_selection'.
The nested function 'close_it' makes it so the button in the new window closes the new window."""
def top_window(window=None, selection=None):
    new_window = Toplevel()
    new_window.title("Your hunter is...")
    new_window.geometry("300x200")

    def close_it():
        new_window.destroy()

    hunter_announce = Label(new_window,text="Your hunter is")
    ta_da = Label(new_window,text=selection)
    hunter_announce.pack()
    ta_da.pack()

    close_window = Button(new_window,
        text="Thank You!",
        width=20,
        height=4,
        command=close_it
    )
    close_window.pack()

"""Updates the json database of hunters based on user input.
Checks the output of 'chosen_ones' against the 'hunter_list'.
If the names in 'chosen_ones' are in 'hunter_list', makes the appropriate value 'true'.
Otherwise, makes it 'false'."""
def update_json(hunter_list=None,ugly_child=None):
    data = hunter_list
    for i in data:
        if i in ugly_child:
            data[i] = True
        else:
            data[i] = False
    with open('hunter_list.json', 'w') as f:
        json.dump(data,f)

"""The button that pulls all this nonsense together."""
def the_button(hunter_list_numbers=None,
               selection_prompt=None,
               window=None):
    chosen_ones = ugly_child(get_numbers=get_numbers(hunter_list_numbers),
                             hunter_names=hunter_names(hunter_list()))
    selection = random_hunter_selection(ugly_child=chosen_ones)
    top_window(window,selection)
    selection_prompt.config(text=selection)
    update_json(hunter_list=hunter_list(),
                ugly_child=chosen_ones)