from os import error


while True:
    try:   
        def strip(string):
            return string.strip()

        def show_content():
            rows = []
            contacts = open("contacts.db", 'r', encoding="utf-8")
            for row in contacts:
                rows.append(list(map(strip, row.split(", "))))
            print("List of current users in contacts.db:\n",*rows,sep="\n")
            contacts.close()
            print()

        def write_content():
            contacts = open("contacts.db", 'a', encoding="utf-8")
            print("To abort user creation, input q1")
            name = input("Input your name (e.g. name surname): ")
            if name == "q1":
                contacts.close()
                main()
            else:
                pass
            phone = input("Input your phone (e.g. +372 123 5678): ")
            if phone == "q1":
                contacts.close()
                main()
            else:
                pass
            age = input("Input your age (e.g. 17): ")
            if age == "q1":
                contacts.close()
                main()
            else:
                pass
            email = input("Input your email (e.g. example@example.org): ")
            if email == "q1":
                contacts.close()
                main()
            else:
                pass
            data = name+", "+phone+", "+age+", "+email
            input("Success!\nPress any key to continue.")
            print(data)
            contacts.write(("{}\n".format(data)))
            contacts.close()

        def edit_content():
            contacts = open("contacts.db", 'r', encoding="utf-8")
            content = contacts.readlines()
            print(*content)
            choice = input("To abort editing, type 'q'\n\nWhat line you would like to edit: ")
            if choice == "q":
                contacts.close()
                main()
            else:
                pass
            i = int(choice)
            choice = int(choice)
            i = contacts.seek(choice)
            if i == choice:
                i = i-1
                print(content[i])
                print("Insert new information")
                contacts = open("contacts.db", 'a', encoding="utf-8")
                name = input("Input new name (e.g. name surname): ")
                phone = input("Input new phone (e.g. +372 123 5678): ")
                age = input("Input new age (e.g. 17): ")
                email = input("Input new email (e.g. example@example.org): ")
                data = name+", "+phone+", "+age+", "+email
                content[i] = data
                contacts.close()
                contacts = open("contacts.db", 'w', encoding="utf-8")
                newdata = "".join(content)
                print(newdata)
                contacts.write(newdata)
                contacts.close()
                input("Success!\nPress any key to continue.")

        def delete_content():
            contacts = open("contacts.db", 'r', encoding="utf-8")
            data = contacts.readlines()
            contacts.close()
            contacts = open("contacts.db", 'w', encoding="utf-8")
            for line in data:
                if line.strip("\n") != ", , , ":
                    contacts.write(line)
            contacts.close()
            input("Success!\nPress any key to continue.")

        def print_out_commands():
            print("Commands are:")
            print("1. list users")
            print("2. edit user")
            print("3. add user")
            print("9. del user")
            usr = int(input("Input desired number: "))
            if usr == 1:
                print(show_content())
            if usr == 2:
                edit_content()
            if usr == 3:
                write_content()
            if usr == 9:
                print("To delete a user you should edit user line and fill it with blanks (basically ENTER all prompts)\n afterwards use DEL USER command.")
                print("\nTo delete blanks users, press Y.\nTo abort press N.")
                user = input("Delete blanks users? y/N: ")
                if user == "Y": 
                    delete_content()
                if user == "N" or user == "None":
                    main()
                        
                
        def main():
            show_content()
            print_out_commands()

        main()

    except:
        print("Something went wrong. Try again.")
        continue