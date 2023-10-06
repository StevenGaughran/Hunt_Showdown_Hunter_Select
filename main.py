import random
import tkinter.scrolledtext
from tkinter import *
import hunter_data as hd

"""This fills in the window with hunter names, and pre-selects them if they are 'owned'."""
hunter_list_numbers = []
def populate_hunter_list():
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

# Tkinter setup
window = Tk()
window.title("Rise up, dead man! A 'Hunt: Showdown' random hunter selector!")
greeting = Label(text="Rise up, dead man!")
greeting.pack()

selection_prompt = Label(text="YOUR NEXT HUNTER IS...")
selection_prompt.pack()

# Tkinter Text
text = tkinter.scrolledtext.ScrolledText()
text.pack()

populate_hunter_list()

# The button that runs the function that randomly selects your Hunter.
def the_button():
    # list_numbers = hunter_list.curselection()
    # # This writes the index locations of selected numbers to a Word file, for future list pre-generation.
    # with open ("hunter_list_index.txt", "w") as edit:
    #     edit.truncate(0)
    #     edit.write(str(list_numbers))
    #
    # # This gives you your randomly selected hunter.
    # selection_list = []
    # for i in list_numbers:
    #     y = hunter_list.get(first=i)
    #     selection_list.append(y)
    # selection_prompt.config(text=random.choice(selection_list))
    pass


run_it = Button(
    text="Choose your fate!",
    width=20,
    height=4,
    command=the_button
)
run_it.pack()

# Required code for Tkinter.
window.mainloop()
