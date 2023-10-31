import json
import random
from tkinter import IntVar,Checkbutton,Toplevel,Label,Button

def hunter_list():
    """Loads a list of hunters from the file `hunter_list.json` and returns it.

    Returns:
        A dictionary of hunters with true/false values.
        True values indicated "owned" hunters.
        False values indicate "unowned" hunters.
    """
    with open("hunter_list.json", "r") as i:
        hunters = json.load(i)
    return hunters

def owned_hunters(hunter_list=None):
    """Creates a list of "owned" hunters.

    Args:
        hunter_list: json data from 'hunter_list()'.

    Returns:
        A list of all hunter names with a 'true' value.
    """
    owned = [k for k, v in hunter_list.items() if v == True]
    return owned

def unowned_hunters(hunter_list=None):
    """Creates a list of "unowned" hunters.

    Args:
        hunter_list: json data from 'hunter_list()'.

    Returns:
        A list of all hunter names with a 'false' value.
    """
    unowned = [k for k, v in hunter_list.items() if v == False]
    return unowned

# Creates a list of Hunter names derived from 'hunter_list'
def hunter_names(hunter_list=None):
    """Creates a list of all hunter names.

    Args:
        hunter_list: json data from 'hunter_list()'.

    Returns:
        A list of all hunter names, derived from 'hunter_list()' keys.
    """
    h_list = []
    for i in hunter_list:
        h_list.append(i)
    return h_list

def populate_hunter_list(text=None):
    """This fills in the window with checkbuttons and hunter names.
    Pre-selects them if they are 'owned'.
    Populates the hunter_list_numbers with returned IntVars.

    Args:
        text: 'scrolledtext.ScrolledText()' in 'main.py'.

    Returns:
        A list populated by checkbutton IntVars.
    """
    hunter_list_numbers = []
    for i in hunter_list():
        if i in owned_hunters(hunter_list()):
            var = IntVar()
            cb = Checkbutton(text=i,
                             bg='black',
                             fg='white',
                             selectcolor='black',
                             anchor='w',
                             variable=var)
            cb.select()
            hunter_list_numbers.append(var)
            text.window_create('end', window=cb)
            text.insert('end', '\n')
        elif i in unowned_hunters(hunter_list()):
            var = IntVar()
            cb = Checkbutton(text=i,
                             bg='black',
                             fg='white',
                             selectcolor='black',
                             anchor='w',
                             variable=var)
            hunter_list_numbers.append(var)
            text.window_create('end', window=cb)
            text.insert('end', '\n')
    return hunter_list_numbers

def get_numbers(hunter_list_numbers=None):
    """Extracts 0 and 1 IntVar values.

    Args:
        hunter_list_numbers: IntVars from 'hunter_list_numbers()'.

    Returns:
        A list populated by IntVar values, either 0 or 1.
    """
    number_list = []
    for i in hunter_list_numbers:
        x = i.get()
        number_list.append(x)
    return number_list

def ugly_child(get_numbers=None, hunter_names=None):
    """Gets the hunter names necessary for random selection.
    Takes the two lists and creates an index.
    Uses the index to pull the appropriate names.

    Args:
        get_numbers: numbers from 'get_numbers()'.
        hunter_names: names from 'hunter_names()'.

    Returns:
        A list names in string format.
    """
    chosen_ones = []
    for index, element in enumerate(get_numbers):
        if element == 1:
            chosen_ones.append(hunter_names[index])
    return chosen_ones

def random_hunter_selection(ugly_child=None):
    """Randomly selects a hunter name.

    Args:
        ugly_child: the list of names to select from randomly.

    Returns:
        A single name in string format.
    """
    selection = random.choice(ugly_child)
    return selection

def top_window(window=None, selection=None):
    """Creates a new window to place the selected hunter name.

    Args:
        window: 'window' from 'main.py'.
        selection: The name chosen from 'random_hunter_selection()'.
    """
    new_window = Toplevel()
    new_window.title("Your hunter is...")
    new_window.geometry("300x150")
    new_window.configure(bg='black')

    def close_it():
        """Destroys the top window when the button is pressed."""
        new_window.destroy()

    hunter_announce = Label(new_window,text="Your hunter is", fg='white', bg='black')
    ta_da = Label(new_window,text=selection, fg='white', bg='black', font=('Arial', 25))
    hunter_announce.pack()
    ta_da.pack()

    close_window = Button(new_window,
        text="Thank You!",
        width=15,
        height=2,
        command=close_it
    )
    close_window.pack()

def try_again_window():
    """A window that pops up if you try and pull a random hunter using 'the_button', but no hunters are selected."""
    new_window = Toplevel()
    new_window.title("No hunters selected!")
    new_window.geometry("200x70")
    new_window.configure(bg='black',
                         padx=2,
                         pady=2)

    no_hunters = Label(new_window, text="Please select at least ONE hunter.", fg='white', bg='black')
    no_hunters.pack()

    def close_it():
        """Destroys the top window when the button is pressed."""
        new_window.destroy()

    close_window = Button(new_window,
                          text="Thank You!",
                          width=15,
                          height=2,
                          command=close_it
                          )
    close_window.pack()

def update_json(hunter_list=None,ugly_child=None):
    """Updates the json database of hunters based on checkbox input.
    Checks the output of 'chosen_ones' against the 'hunter_list'.
    If the names in 'chosen_ones' are in 'hunter_list', makes the appropriate value 'true'.
    Otherwise, makes it 'false'.

    Args:
        hunter_list: names from 'hunter_list()'.
        ugly_child: names from 'ugly_child()'.
    """
    data = hunter_list
    for i in data:
        if i in ugly_child:
            data[i] = True
        else:
            data[i] = False
    with open('hunter_list.json', 'w') as f:
        json.dump(data,f)

def the_button(hunter_list_numbers=None,
               selection_prompt=None,
               window=None):
    """The button that you press to make this beautiful disaster work.

    Args:
        hunter_list_numbers: numbers from 'hunter_list_numbers()'.
        selection_prompt: 'selection_prompt' from 'main.py'.
        window: 'window' from 'main.py'.
    """
    try:
        chosen_ones = ugly_child(get_numbers=get_numbers(hunter_list_numbers),
                             hunter_names=hunter_names(hunter_list()))
        selection = random_hunter_selection(ugly_child=chosen_ones)
        top_window(window,selection)
        update_json(hunter_list=hunter_list(),
                    ugly_child=chosen_ones)
    except IndexError:
        try_again_window()

# Select All and Deselect All buttons.
def select_all_checkbuttons(hunter_list_numbers=None):
    """Sets all checkbuttons from 'hunter_list_numbers' in 'main.py' to Selected.

    Args:
        hunter_list_numbers: the IntVars from 'hunter_list_numbers' in 'main.py'.
    """
    for var in hunter_list_numbers:
        var.set(1)

def deselect_all_checkbuttons(hunter_list_numbers=None):
    """Sets all checkbuttons from 'hunter_list_numbers' in 'main.py' to Deselected.

    Args:
        hunter_list_numbers: the IntVars from 'hunter_list_numbers' in 'main.py'.
    """
    for var in hunter_list_numbers:
        var.set(0)
