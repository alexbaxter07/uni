import os
import csv

def main():
    print("")
    print("####################################################")
    print("############## SHU Library management System ##############")
    print("####################################################")
    print("")
    print("########### Please select an option ################")
    print("### 1. Login")
    print("### 200. Exit program")
    # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it
    print("")

    #the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later
    choice = int(input("Please select an option (n): "))

    #double equals signs is a comparison which will return a boolean
    if choice == 1:
        user = login()

        if user["Role"] == "Librarian":
            lib_main_menu()

        elif user["Role"] == "Supervisor":
            sup_main_menu()

    elif choice == 200:
        quit()  # this function will stop the program

    else:
        print("Your choice was invalid please try again")

def login():


    email = input("Please enter your email: ").strip()
    password = input("Please enter your password: ").strip()

    with open('staff.csv') as file:

        for line in file.readlines():






# this is a secure way of calling main
if __name__ == '__main__':
    main()
