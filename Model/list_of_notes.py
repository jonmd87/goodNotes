from Model.constants import *


def list_of_notes(notes_dict):
    for key in notes_dict:
        print(f"DATE: {key}\t\tTITLE: "
              f"{notes_dict[key][0]}"
              f"\n\t\t\t{notes_dict[key][1]}")
