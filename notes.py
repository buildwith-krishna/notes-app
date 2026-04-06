def main():

    print("<---WELCOME TO NOTES APP--->" + "\n")
    
    while True:
    
        print("<---Choose your option--->" + "\n")
        print("1. Add a note")
        print("2. view notes")
        print("3. exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            note = input("Enter your note: ")

            with open("notes2.txt", "a") as file:
                file.write(note + "\n")

            print("<--Note added successfully-->") 

        elif choice == "2":
            try:
                with open("notes2.txt", "r") as file:
                    print(file.read())
                    
            except FileNotFoundError:
                print("Note is empty! Please add a note first.")

        elif choice == "3":
            print("Goodbye")
            break        

        else: 
            print("Invalid input! Please enter choice from 1 to 3.")

            
main()
