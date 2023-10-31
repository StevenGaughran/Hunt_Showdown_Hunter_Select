from tkinter import Tk,Label,scrolledtext,Button
import hunter_data as hd

"""The setup for the Tkinter GUI."""
# Tkinter setup
window = Tk()
window.iconbitmap('icon.ico')
window.geometry('200x600')
window.configure(bg='black',
                 pady=2,
                 padx=2)
window.title("Rise up, dead man! A 'Hunt: Showdown' random hunter selector!")
greeting = Label(text="Rise up, dead man!",
                 bg='black',
                 fg='white')
greeting.pack()

selection_prompt = Label(text="YOUR NEXT HUNTER IS...",
                         fg='white',
                         bg='black',
                         pady=8)
selection_prompt.pack()

# Tkinter Text
text = scrolledtext.ScrolledText(bg='black',
                                 fg='white',
                                 relief='solid',
                                 borderwidth=5,
                                 pady=2,
                                 padx=2)
text.pack()

"""Calling the 'populate_hunter_list' function and storing the checkbutton IntVar values in a variable."""
hunter_list_numbers = hd.populate_hunter_list(text=text)

"""The Tkinter Buttons"""
run_it = Button(
    text="Choose your fate!",
    width=20,
    height=4,
    borderwidth=5,
    command=lambda: hd.the_button(hunter_list_numbers=hunter_list_numbers,
                                  selection_prompt=selection_prompt,
                                  window=window)
)
run_it.pack()

select_all = Button(
    text="Select All",
    width=10,
    height=2,
    command=lambda: hd.select_all_checkbuttons(hunter_list_numbers=hunter_list_numbers)
)
select_all.pack(side='left')

deselect_all = Button(
    text="Deselect All",
    width=10,
    height=2,
    command=lambda: hd.deselect_all_checkbuttons(hunter_list_numbers=hunter_list_numbers)
)
deselect_all.pack(side='right')

# Required code for Tkinter.
window.mainloop()
