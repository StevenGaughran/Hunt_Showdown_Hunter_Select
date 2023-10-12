import random
from tkinter import Tk,Label,scrolledtext,Button
import hunter_data as hd

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

"""# Calling the 'populate_hunter_list' function and storing the checkbutton IntVar values in a variable."""
hunter_list_numbers = hd.populate_hunter_list(text=text)

"""The Button that spits up a random selection.
Currently here, but will probably be relocated to the GUI file in the future."""
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
    # command=hd.the_button(hunter_list_numbers)
)
run_it.pack()

# Required code for Tkinter.
window.mainloop()
