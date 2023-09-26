import random

# ~~~ Reads a .txt file that contains all legendary hunters in the game ~~~
def compiled_hunter_list():
    my_file = open("hunters.txt", "r")
    data = my_file.read()
    hunter_list = data.split("\n")
    my_file.close()
    return hunter_list

# ~~~ Randomly selects a hunter from "compiled_hunter_list" ~~~
def random_hunter_selection(hunters):
    selection = random.choice(hunters)
    print(selection)

# ~~~ Generates a dictionary from "compiled_hunter_list" ~~~
# ~~~ This is for future use in organizing owned/unowned hunters ~~~
def hunt_dict(data):
    big_dict = {}
    for i in data:
        big_dict[i] = False
    return big_dict

# ~~~ Sorting the True/False data from "hunt_dict" ~~~
def sorting(mess):
    return list(mess.keys()),[list(mess.values()).index(False)]

sorting(hunt_dict(compiled_hunter_list()))
