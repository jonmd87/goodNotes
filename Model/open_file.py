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
    temp_dict = {}
    if check_if_file_exist() == 0:
        with open(FILE_PATH, "w") as file_csv:
            reader = csv.DictReader(file_csv)
            for line in reader:
    return temp_dict


def write_file(notes_dict):
        with open(FILE_PATH, "w") as file_csv:
            writer = csv.writer(file_csv, delimiter=';')
            writer.writerows(notes_dict)
