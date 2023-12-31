from os import name
from webbrowser import get

def InputData():
    while True:
        first_name = input("Insert your first name: ")
        if not (first_name.isalpha()):
            print("Invalid first name")
            print()
        else:
            print("-------------------------------")
            print()
            break

    while True:
        last_name = input("Insert your last name: ")
        if not (last_name.isalpha()):
            print("Invalid last name")
            print()
        else:
            print("--------------------------------")
            print()
            break

    while True:
        studyYear = input("Insert your year of study: ")
        if studyYear.isdigit() and int(studyYear) == 2023:
            print("--------------------------------")
            print()
            break
        print("Invalid study year.")
        print()

    while True:
        final_campus = input("Insert the campus you will be attending: ")
        if final_campus.lower() in ["cape town", "johannesburg", "pretoria", "durban", "rustenburg"]:
            print("--------------------------------")
            print()
            break
        else:
            print("Invalid campus")
            print()

    create_user_name(first_name, last_name, studyYear, final_campus)


def create_user_name(first_name, last_name, studyYear, final_campus):
    username = first_name[-3:].lower() if len(first_name) >= 3 else first_name.upper() + "O"
    username += last_name[:3].lower() + campus(final_campus) + studyYear[-2:]

    print(f"Final username: {username}")

    if username_exists(username):
        print("Username already exists.")
        choice = input("Do you want to start again? (yes/no): ")
        if choice.lower() == "yes":
            print()
            InputData()
            return 
        else:
            print("Exiting the program.")
            return

    confirmation = input("Is the username correct? (yes/no): ")
    if confirmation.lower() == "yes":
        save_username_to_file(username, first_name, last_name, studyYear, final_campus)
    else:
        print("Please run the program again to generate a new username.")
     
    return username



def campus(campus):
    valid_campuses = {"cape town": "cpt", "johannesburg": "jhb", "pretoria": "pta", "durban": "dbn", "rustenburg": "rus"}
    return valid_campuses.get(campus.lower(), "")


def username_exists(new_username):
    with open("username.txt", "r") as file:
        for line in file:
            if "Username:" in line:
                existing_username = line.split(":")[1].strip()
                if existing_username == new_username:
                    return True
    return False

def save_username_to_file(username, first_name, last_name, studyYear, final_campus):
    with open("username.txt", "a") as file:
        file.write(f"First Name: {first_name}\n")
        file.write(f"Last Name: {last_name}\n")
        file.write(f"Study Year: {studyYear}\n")
        file.write(f"Campus: {final_campus}\n")
        file.write(f"Username: {username}\n")
        file.write(f"===================================\n")
    print("Your data has been saved to username.txt")


if __name__ == '__main__':
    InputData() 