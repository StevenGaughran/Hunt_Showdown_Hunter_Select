"""Placeholder file.
Eventually, this is where I'm going to be creating the actual Tkinter GUI."""
from tkinter import Tk,Label,scrolledtext

class Gui:
    def __init__(self):
        window = Tk()
        window.title("Rise up, dead man! A 'Hunt: Showdown' random hunter selector!")
        greeting = Label(text="Rise up, dead man!")
        greeting.pack()

        selection_prompt = Label(text="YOUR NEXT HUNTER IS...")
        selection_prompt.pack()

        # Tkinter Text
        text = scrolledtext.ScrolledText()
        text.pack()
