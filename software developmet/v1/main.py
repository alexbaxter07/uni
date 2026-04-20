import pandas as pd #this imports pandas which is used for data wrangling
import matplotlib.pyplot as plt #this imports matplotlib which is used for creating graphs from the dataframes

def main():
    print("")
    print("####################################################")
    print("############## SHU Library management System ##############")
    print("####################################################")
    print("")
    print("########### Please select an option ################")
    print("### 1. Librarian Login")
    print("### 2. Supervisor Login")
    print("### 200. Exit program")
    # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it
    print("")

    #the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later
    choice = int(input("Please select an option (n): "))

    #double equals signs is a comparison which will return a boolean
    if choice == 1:
        lib_main_menu()

    elif choice == 2:
        sup_main_menu()

    elif choice == 200:
        quit()  # this function will stop the program

    else:
        print("Your choice was invalid please try again")


def sup_main_menu():

    while True:

        print("")
        print("####################################################")
        print("############## Library management System ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Loan a book")
        print("### 2. Return a book")
        print("### 3. View A Book")
        print("### 4. Manage Staff")
        print("### 5. Add A Book")
        print("### 200. Exit program")
        # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it

        # the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later
        choice = int(input("Please select an option (n): "))

        if choice == 1:
            source = book_loan()
            print("This is the book you are loaning:")
            print(source)

        elif choice == 2:
            source = book_return()
            print("This is the book you have returned:")
            print(source)

        elif choice == 3:
            source = book_veiw()
            print("This is the list of available books:")
            print(source)

        elif choice == 200:
            quit()  # this function will stop the program

        else:
            print("Your choice was invalid please try again")

def lib_main_menu():

    while True:

        print("")
        print("####################################################")
        print("############## Library management System ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Loan a book")
        print("### 2. Return a book")
        print("### 3. View A Book")
        print("### 200. Exit program")
        # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it

        # the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later
        choice = int(input("Please select an option (n): "))

        if choice == 1:
            source = book_loan()
            print("This is the book you are loaning:")
            print(source)

        elif choice == 2:
            source = book_return()
            print("This is the book you have returned:")
            print(source)

        elif choice == 3:
            source = book_veiw()
            print("This is the list of available books:")
            print(source)

        elif choice == 200:
            quit()  # this function will stop the program

        else:
            print("Your choice was invalid please try again")

# this is a secure way of calling main
if __name__ == '__main__':
    main()
