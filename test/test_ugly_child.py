import pytest
import random
import json
from hunter_data import ugly_child, random_hunter_selection, hunter_list
from tkinter import IntVar

# Four functions that test the 'hunter_list' function.
@pytest.mark.skip(reason="Passed")
def test_hunter_list_file_exists():
    # Check if the 'hunter_list.json' file exists
    with open("../hunter_list.json", "r") as file:
        pass  # If the file doesn't exist, an error will be raised here

# Having trouble with the following three functions.
# They can't seem to find 'hunter_list.json'?
def test_hunter_list_returns_dict():
    # Check if the function returns a dictionary
    result = hunter_list()
    assert isinstance(result, dict)

def test_hunter_list_dict_structure():
    # Check the structure of the returned dictionary
    result = hunter_list()
    expected_structure = {
        "hunter1": bool,
        "hunter2": bool,
        # Add more keys for other hunters if needed
    }

    for key, value_type in expected_structure.items():
        assert key in result
        assert isinstance(result[key], value_type)

def test_hunter_list_file_contents():
    # Check if the file contents match the returned dictionary
    with open("../hunter_list.json", "r") as file:
        file_data = json.load(file)

    result = hunter_list()
    assert result == file_data

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
    picked_one = random_hunter_selection(chosen_ones)
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
# Change first 'for' loop to look through the big_hunter_list, not chosen_ones.
def test_update_hunter_list():
    chosen_ones = ["Jan", "Casey"]
    big_hunter_list = {"Jan": False,
                       "Casey": True,
                       "Scott": False,
                       "Steve": True}
    for i in big_hunter_list:
        if i in chosen_ones:
            big_hunter_list[i] = True
        else:
            big_hunter_list[i] = False
    assert big_hunter_list == {"Jan": True,
                               "Casey": True,
                               "Scott": False,
                               "Steve": False}

@pytest.mark.skip(reason="Works")
def test_random_selection():
    chosen_ones = ["Bill", "Harry", "Karl"]
    selection = random.choice(chosen_ones)
    assert selection in chosen_ones
