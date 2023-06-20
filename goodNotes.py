GREETING = "Hello, this is application for notes."
GOODBYE = "Goodbye!!!"
CHOOSE = "Choose: "
ERROR = "Error. Wrong number."
CREATE_NOTE = "1. Create a note."
LIST_OF_NOTES = "2. List of notes."
CHANGE_NOTE = "3. Change note."
DELETE_NOTE = "4. Delete note."
EXIT = "0. Exit."



def menu():
    print(CREATE_NOTE)
    print(LIST_OF_NOTES)
    print(CHANGE_NOTE)
    print(DELETE_NOTE)
    print(EXIT)


def create_new_note():
    print("create new note")


def list_of_notes():
    print("list of notes")

def change_note():
    print("change note")

def delete_note():
    print("delete note")

def get_answer():
    answer = str(input(CHOOSE))
    
    return answer


def make_something(answer):
    match answer:
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


print(GREETING)
answer = -1
while answer != 0:
    menu()
    answer = get_answer()
    make_something(answer)
print(GOODBYE)
