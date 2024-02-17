from course import Course

TU257 = Course("TU257")

def print_menu():
    print("----------------")
    print("Select an option:")
    print("1. Create a Student")
    print("2. Display Student List")
    print("3. Update a Student")
    print("4. Delete a Student")
    print("----------------")

#********************************

while True:
    print_menu()
    option = input("Please make a choice >> ")

    if option == "1":
        new_name = input("enter a student name: ")
        TU257.student_list.append(new_name)
    elif option =="2":
        TU257.display_all()
    elif option == "3":
       print("Update student")
    elif option == "4":
       print("Delete student")
    else: 
       print("Invalid option, please try again")

    input("Press enter to continue.......1")
    








