import datetime


def add_new_note(notes_dict, new_note):
    curr_time = str(datetime.datetime.now())
    notes_dict[curr_time] = new_note
    notes_dict = dict(sorted(notes_dict.items()))
