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

run_it = Button(
    text="Choose your fate!",
    width=20,
    height=4,
    command=lambda: hd.the_button(hunter_list_numbers=hunter_list_numbers, selection_prompt=selection_prompt)
)
run_it.pack()

# Required code for Tkinter.
window.mainloop()
