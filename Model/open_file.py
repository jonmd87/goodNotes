import os.path

from Model.constants import *
import csv


def check_if_file_exist():
    check = 0
    if not os.path.isdir(PATH):
        os.mkdir(PATH)
        check = 1
    if not os.path.exists(FILE_PATH):
        file_csv = open(FILE_PATH, "w")
        file_csv.close()
        check = 2
    return check


def open_file():
    tmp_dict = {}
    if check_if_file_exist() == 0:
        with open(FILE_PATH, "r") as file_csv:
            reader = csv.reader(file_csv)
            for line in reader:
                tmp_lst = line[0].split(';')
                tmp_dict[tmp_lst[0]] = [tmp_lst[1], tmp_lst[2]]
    return tmp_dict


def write_file(notes_dict):
    with open(FILE_PATH, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=DELIMETR)
        for key in notes_dict:
            writer.writerow([key, notes_dict[key][0], notes_dict[key][1]])
