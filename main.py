import random
from tkinter import Tk,Label,scrolledtext,Button,IntVar,Checkbutton
import hunter_data as hd

"""This fills in the window with hunter names, and pre-selects them if they are 'owned'.
Populates the hunter_list_numbers with returned IntVars."""

def populate_hunter_list():
    hunter_list_numbers = []
    for i in hd.hunter_list():
        if i in hd.owned_hunters(hd.hunter_list()):
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
        elif i in hd.unowned_hunters(hd.hunter_list()):
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

"""The setup for the Tkinter GUI.
Will eventually be made its own Class in another document.
For now, it works."""
# Tkinter setup
window = Tk()
window.title("Rise up, dead man! A 'Hunt: Showdown' random hunter selector!")
greeting = Label(text="Rise up, dead man!")
greeting.pack()

selection_prompt = Label(text="YOUR NEXT HUNTER IS...")
selection_prompt.pack()

# Tkinter Text
text = scrolledtext.ScrolledText()
text.pack()

# Calling the function
hunter_list_numbers = populate_hunter_list()

"""The Button that spits up a random selection.
Currently here, but will probably be relocated to the GUI file in the future."""
run_it = Button(
    text="Choose your fate!",
    width=20,
    height=4,
    command=hd.the_button
)
run_it.pack()

# Required code for Tkinter.
window.mainloop()
