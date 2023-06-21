from Model.get_answer import get_answer
from Model.menu import menu
from Presenter.make_something import make_something

GREETING = "Hello, this is application for notes."
GOODBYE = "Goodbye!!!"
CHOOSE = "Choose: "


print(GREETING)
answer = -1
while answer != 0:
    menu()
    answer = get_answer()
    make_something(answer)
print(GOODBYE)
