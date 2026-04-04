def main():

    print("<---WELCOME TO NOTES APP--->")
    
    while True:
        print("1. Add a note")
        print("2. View notes")
        print("3. Exit")

        user = input("Enter the choice: ").strip()

        if user == "3":
            print("Goodbye!") 
            break

        elif user == "1":
            user2 = input("Enter notes (saperated by comma): ") 

            with open("notes.txt", "a") as file:
                file.write(user2 + "\n")

            print("Note added successfully!")
        elif user == "2":
            with open("notes.txt", "r") as file:
                print(file.read())
                print(type(file))
        else:
            print("Invalid input! Please enter number followed by choices.")
            

main()
