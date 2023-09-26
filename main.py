import random
from tkinter import *
import hunter_data as hd


# ~~~ BASIC SETUP STUFF ~~~
window = Tk()
window.title("Rise up, dead man! A 'Hunt: Showdown' random hunter selector!")
greeting = Label(text="Rise up, dead man!")
greeting.pack()

selection_prompt = Label(text="YOUR NEXT HUNTER IS:")
selection_prompt.pack()

# ~~~ List Box ~~~
hunter_list = Listbox(selectmode=MULTIPLE)
hunter_list.pack(side=LEFT,fill=BOTH)
scrollbar = Scrollbar()
scrollbar.pack(side=RIGHT,fill=BOTH)
hunter_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=hunter_list.yview)
for i in hd.compiled_hunter_list():
    hunter_list.insert(END, i)

# ~~~ THE BUTTON ~~~
def the_button():
    list_numbers = hunter_list.curselection()
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

# ~~~ REQUIRED CODE ~~~
window.mainloop()
