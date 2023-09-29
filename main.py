import random
from tkinter import *
import hunter_data as hd


# Pulls the listbox location data from the 'hunter_list_index.txt' file.
# Part of my attempt to pre-select from previously selected hunters.
# This is a messy solution based on index location of imported list.
# Will have problems down the line when new hunters are added.
# Probably best if I used true/false values of the "hunter_list.json" file.
def loc_data():
    with open("hunter_list_index.txt", "r") as pull:
        # the 'eval()' command returns the string as a tuple that doesn't go nuts when I try to access it.
        data = eval(pull.read())
    return data

# This fills in the listbox with hunter names.
def populate_hunter_list():
    for i in hd.hunter_list():
        hunter_list.insert(END, i)
    # What follows is my most recent attempt to get the listbox to pre-generate with old hunters selected.
    # I am VERY CLOSE.
    # Currently, it selects everything UP TO the last item in the loc_data...which it leaves unselected.
    # At least it's selecting items now...

    # I will probably have to change this ENTIRE DOCUMENT to be checkbutton widgets instead of a listbox.
    # Frustrating!
        # last_index = hunter_list.index(END)
        # if last_index in loc_data():
        #     hunter_list.selection_set(last_index, ACTIVE)
        # else:
        #     pass

# Tkinter setup
window = Tk()
window.title("Rise up, dead man! A 'Hunt: Showdown' random hunter selector!")
greeting = Label(text="Rise up, dead man!")
greeting.pack()

selection_prompt = Label(text="YOUR NEXT HUNTER IS...")
selection_prompt.pack()

# The Tkinter listbox
hunter_list = Listbox(selectmode=MULTIPLE)
hunter_list.pack(side=LEFT,fill=BOTH)

scrollbar = Scrollbar()
scrollbar.pack(side=RIGHT,fill=BOTH)

hunter_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=hunter_list.yview)

populate_hunter_list()

# The button that runs the function that randomly selects your Hunter.
def the_button():
    list_numbers = hunter_list.curselection()
    # This writes the index locations of selected numbers to a Word file, for future list pre-generation.
    with open ("hunter_list_index.txt", "w") as edit:
        edit.truncate(0)
        edit.write(str(list_numbers))

    # This gives you your randomly selected hunter.
    selection_list = []
    for i in list_numbers:
        y = hunter_list.get(first=i)
        selection_list.append(y)
    selection_prompt.config(text=random.choice(selection_list))

run_it = Button(
    text="Choose your fate!",
    width=20,
    height=4,
    command=the_button
)
run_it.pack()

# Required code for Tkinter.
window.mainloop()
