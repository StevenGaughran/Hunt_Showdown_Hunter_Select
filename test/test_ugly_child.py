import pytest
import random
from hunter_data import ugly_child, the_selection
from tkinter import IntVar

@pytest.mark.skip
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

@pytest.mark.skip(reason="Bad test, please ignore.")
def test_get_numbers():
    numbers = IntVar()
    numbers.set(100)
    for i in numbers:
        number_list = []
        x = i.get()
        number_list.append(x)
    assert x == [100]

@pytest.mark.skip(reason="Success!")
def test_update_hunter_list():
    chosen_ones = ["Jan", "Casey"]
    big_hunter_list = {"Jan": False,
                       "Casey": True,
                       "Scott": False}
    for i in chosen_ones:
        if i in big_hunter_list:
            big_hunter_list[i] = True
        else:
            big_hunter_list[i] = False
    assert big_hunter_list == {"Jan": True,
                               "Casey": True,
                               "Scott": False}

def test_random_selection():
    chosen_ones = ["Bill", "Harry", "Karl"]
    print(random.choice(chosen_ones))

