from Model.get_answer import get_answer
from Model.menu import menu
from Presenter.make_something import make_something
from Model.open_file import open_file
from Model.constants import *


print(GREETING)
answer = -1
notes_dict = open_file()
while answer != 0:
    menu()
    answer = get_answer()
    make_something(answer, notes_dict)
print(GOODBYE)
