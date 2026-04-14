FILE_NAME = "notes.txt"
            
def add_note():

    note = input("Enter your note: ").strip()
    
    if note == "":
        print("Notes cannot be empty!" + "\n")
    else:
        with open(FILE_NAME, "a") as file:
            file.write(note.strip() + "\n")
            print("<--Note added successfully-->" + "\n")


def get_notes():

    try:
        with open(FILE_NAME, "r") as file:
            notes = file.read().split("\n")

            clean_notes = []
            for note in notes:
                if note != "":
                    clean_notes.append(note)
                
            return clean_notes

    except FileNotFoundError:
        return []

    except Exception as E:
        print(f"Unexpected error: {E}")
        return []

        
def display_notes(clean_notes):
                
    for i, note in enumerate(clean_notes, start=1):

        if note == "":
            print("^Notes are empty!^")
        else:
            print(f"{i}. {note}")
    
def del_note(clean_notes):

    display_notes(clean_notes)
    print("\n")
            
    try:         
        index = int(input("Select index: ").strip())
        print("\n")
    except ValueError:
        print("invaid input! Enter numbers only.")

    if index <= len(clean_notes) and index >= 1:                
        modified_notes = []
        for i, note in enumerate(clean_notes, start=1):
            if i != index:
                modified_notes.append(note)

        with open(FILE_NAME, "w") as file:
            file.write("\n".join(modified_notes) + "\n")    
        print("<<--Note deleted successfully-->>" + "\n")

    else:
        print("That index doesn't exist!")

def update_note(clean_notes):

    print("<<-Choose number to update->>")
    display_notes(clean_notes)
    print("\n")

    try:
        number = int(input("Enter number: ").strip())
    except ValueError:
        print("Enter number of the note only!")
    updated_notes = []
    
    for i, note in enumerate(clean_notes, start=1):
        if i != number:
            updated_notes.append(note)
            
        else:
            new_note = input("Enter new note: ").strip()                
            updated_notes.append(new_note)
            
    with open(FILE_NAME, "w") as file:
        file.write("\n".join(updated_notes) + "\n")

    print("<<--Note updated successfully-->>")
    print("\n")        
            
    
def main():

    notes = get_notes()
    print("<---WELCOME TO NOTES APP--->" + "\n")

    while True:

        print("1. Add a note")
        print("2. View notes")
        print("3. Delete a note")
        print("4. Update a note")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        print("\n")
                
        if choice == "1":
            add_note()
            notes = get_notes()

        elif choice == "2":
            display_notes(notes)
            print("\n")
            
        elif choice == "3":
            del_note(notes)
            notes = get_notes()
            print("\n")

        elif choice == "4":
            update_note(notes)
            notes = get_notes()
            print("\n") 

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid input! Enter choice from 1 to 5." + "\n")

main()
