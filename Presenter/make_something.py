from Model.delete_note import delete_note
from Model.list_of_notes import list_of_notes
from Model.add_new_note import add_new_note
from Model.constants import *
from Model.open_file import write_file


def make_something(choose, notes_dict):
    match choose:
        case 0:
            write_file(notes_dict)
            return
        case 1:
            add_new_note(notes_dict, collect_new_note())
        case 2:
            list_of_notes(notes_dict)
        case 3:
            make_something(4, notes_dict)
            make_something(1, notes_dict)
        case 4:
            delete_note(notes_dict, get_date())
        case _:
            print(ERROR)


def collect_new_note():
    title = str(input(TITLE))
    body = str(input(BODY))
    return [title, body]


def get_date():
    return str(input(DATE))
