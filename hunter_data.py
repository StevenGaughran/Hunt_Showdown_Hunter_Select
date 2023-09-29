import json

# The hunter data.
# Use hunter_list()[0] for the base list, hunter_list()[1] for owned/TRUE hunters, or hunter_list()[2] for unowned/FALSE hunters.
def hunter_list():
    with open("hunter_list.json", "r") as i:
        hunters = json.load(i)
        owned = [k for k, v in hunters.items() if v == True]
        not_owned = [k for k, v in hunters.items() if v == False]
    return hunters

# The following two functions are me compensating for the fact that I couldn't figure something out.
# I figured it out, so they are PROBABLY no longer necessary?
# def owned_hunters(list):
#     owned = [k for k, v in list.items() if v == True]
#     return owned
#
# def unowned_hunters(list):
#     unowned = [k for k, v in list.items() if v == False]
#     return unowned

