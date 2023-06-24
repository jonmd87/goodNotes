from Model.constants import *


def find_note_by_title(notes_dict, date):
    for key in notes_dict:
        key_str = str(key)
        if date == key_str:
            return key
    return None


def delete_note(notes_dict, date):
    key = find_note_by_title(notes_dict, date)
    if key is not None:
        notes_dict.pop(key)
    else:
        print(ERROR)
