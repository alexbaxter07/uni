import pandas as pd #this imports pandas which is used for data wrangling
import matplotlib.pyplot as plt #this imports matplotlib which is used for creating graphs from the dataframes

def main():
    print("")
    print("####################################################")
    print("############## SHU Library management System ##############")
    print("####################################################")
    print("")
    print("########### Please select an option ################")
    print("### 1. Staff Login")
    print("### 2. Student Login")
    print("### 200. Exit program")
    # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it
    print("")

    #the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later
    choice = int(input("Please select an option (n): "))

    #double equals signs is a comparison which will return a boolean
    if choice == 1:
        staff_main_menu()

    elif choice == 2:
        stu_main_menu()

    elif choice == 200:
        quit()  # this function will stop the program

    else:
        print("Your choice was invalid please try again")

def staff_main_menu():

    while True:

        print("")
        print("####################################################")
        print("############## SHU Staff Library management System ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Libarian Menu")
        print("### 2. Supervisor Menu")
        print("### 200. Exit program")
        # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it

        # the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later
        choice = int(input("Please select an option (n): "))

        if choice == 1:
            libarian_main_menu()

        elif choice == 2:
            supervisor_main_menu()

        elif choice == 200:
            quit()  # this function will stop the program

        else:
            print("Your choice was invalid please try again")

def supervisor_main_menu():

    while True:

        print("")
        print("####################################################")
        print("############## Supervisor management System ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Add Staff")
        print("### 2. Remove Staff ")
        print("### 3. Borrow a book")
        print("### 4. Return a book")
        print("### 5. View Available Books")
        print("### 6. View All Books")
        print("### 200. Exit program")
        # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it

        # the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later
        choice = int(input("Please select an option (n): "))

        if choice == 1:
            source = add_staff()
            print("This is the staff member you have added:")
            print(source)

        elif choice == 1:
            source = remove_staff()
            print("This is the staff member you have removed:")
            print(source)
        elif choice == 3:
            source = book_borow()
            print("This is the book you are borrowing:")
            print(source)
        elif choice == 4:
            source = book_return()
            print("This is the book you have returned:")
            print(source)

        elif choice == 5:
            source = available_books()
            print("This is the total income of cash vs card:")
            print(source)

        elif choice == 5:
            source = all_books()
            print("This is all the books in the libary:")
            print(source)

        elif choice == 200:
            quit()  # this function will stop the program

        else:
            print("Your choice was invalid please try again")

def libarian_main_menu():

    while True:

        print("")
        print("####################################################")
        print("############## Library management System ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Borrow a book")
        print("### 2. Return a book")
        print("### 3. View Available Books")
        print("### 4. View All Books")
        print("### 200. Exit program")
        # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it

        # the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later
        choice = int(input("Please select an option (n): "))

        if choice == 1:
            source = book_borow()
            print("This is the book you are borrowing:")
            print(source)

        elif choice == 2:
            source = book_return()
            print("This is the book you have returned:")
            print(source)

        elif choice == 3:
            source = available_books()
            print("This is the total income of cash vs card:")
            print(source)

        elif choice == 200:
            quit()  # this function will stop the program

        else:
            print("Your choice was invalid please try again")

def stu_main_menu():

    while True:

        print("")
        print("####################################################")
        print("############## SHU Student Library management System ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Borrow a book")
        print("### 2. Return a book")
        print("### 3. View Available Books")
        print("### 200. Exit program")
        # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it

        # the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later
        choice = int(input("Please select an option (n): "))

        if choice == 1:
            source = book_borow()
            print("This is the book you are borrowing:")
            print(source)

        elif choice == 2:
            source = book_return()
            print("This is the book you have returned:")
            print(source)

        elif choice == 3:
            source = available_books()
            print("This is the total income of cash vs card:")
            print(source)

        elif choice == 200:
            quit()  # this function will stop the program

        else:
            print("Your choice was invalid please try again")

# this is a secure way of calling main
if __name__ == '__main__':
    main()
