from Model.change_note import change_note
from Model.delete_note import delete_note
from Model.list_of_notes import list_of_notes
from Model.create_new_note import create_new_note

ERROR = "Error. Wrong number."


def make_something(choose):
    match choose:
        case 1:
            create_new_note()
        case 2:
            list_of_notes()
        case 3:
            change_note()
        case 4:
            delete_note()
        case _:
            print(ERROR)
