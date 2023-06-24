from Model.constants import *


def list_of_notes(notes_dict):
    for key in notes_dict:
        date_str = str(key)
        title = notes_dict[key].split(SEPARATOR)[0]
        body = notes_dict[key].split(SEPARATOR)[1]
        print(f"DATE: {date_str}\t\tTITLE: {title}\n\t\t\t{body}")
