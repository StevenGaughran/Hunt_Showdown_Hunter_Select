import pytest
from hunter_data import ugly_child, the_selection
from tkinter import IntVar

def test_happy_day():
    checkbox_selection = [0,1,0,0,1,0]
    hunter_list = ['Bob', 'Jan', 'Fred', 'Carl', 'Casey','Steve']
    chosen_ones = ugly_child(checkbox_selection, hunter_list)
    assert chosen_ones == ["Jan", "Casey"]

@pytest.mark.skip
def test_happy_day_many():
    checkbox_selection = [0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0]
    hunter_list = ['Bob', 'Jan', 'Fred', 'Carl', 'Casey','Steve','Rob','Hans','Scott','Susan','Jen','Sam']
    chosen_ones = ugly_child(checkbox_selection, hunter_list)
    assert chosen_ones == ["Jan", "Casey"]

@pytest.mark.skip(reason="Need to learn the type.")
def test_the_selection():
    chosen_ones = ['a', 'b', 'c']
    picked_one = the_selection(chosen_ones)
    assert picked_one in chosen_ones
    assert type(picked_one) == "c"

def test_get_numbers():
    numbers = IntVar()
    numbers.set(100)
    for i in numbers:
        number_list = []
        x = i.get()
        number_list.append(x)
        assert x == [100]