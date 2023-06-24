from Model.constants import *
def get_answer():
    string = str(input(CHOOSE))
    for char in string:
        if char.isalpha():
            return -1
    return int(string)
