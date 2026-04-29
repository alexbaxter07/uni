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
        login()

    elif choice == 200:
        quit()  # this function will stop the program

    else:
        print("Your choice was invalid please try again")

def login():


    email = input("Please enter your email: ").strip()
    password = input("Please enter your password: ").strip()
    file_path = os.path.join(os.path.dirname(__file__), 'staff.csv')

    with open(file_path) as f:
        reader =csv.DictReader(f)

        for row in reader:

            if row["Status"] == "active":

                if row["Email"] == email and row["Password"] == password:

                    print("Login successful!")

                    if row["Role"] == "Librarian":
                        lib_main_menu()
                        return
                    elif row["Role"] == "Supervisor":
                        sup_main_menu()
                        return

                else:
                    print("Invalid Email or password.")
                    return

            else:
                print("Your account is not active")
                return

def lib_main_menu():

    print("")
    print("####################################################")
    print("############## SHU Library management System ##############")
    print("####################################################")
    print("")
    print("########### Please select an option ################")
    print("### 1. Loan Books")
    print("### 2. Return Books")
    print("### 3. Extend loan period for Books")
    print("### 3.  Search for Books")
    print("### 200. Exit program")
    # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it
    print("")

    choice = int(input("Please select an option (n): "))

    if choice == 1:
        loan()
    elif choice == 2:
        return_book()
    elif choice == 3:
        extend_loan()
    elif choice == 4:
        search()
    elif choice == 200:
        quit()
    else:
        print("Your choice was invalid please try again")

def sup_main_menu():

    print("")
    print("####################################################")
    print("############## SHU Library management System ##############")
    print("####################################################")
    print("")
    print("########### Please select an option ################")
    print("### 1. Loan Books")
    print("### 2. Return Books")
    print("### 3. Extend loan period for Books")
    print("### 3.  Search for Books")
    print("### 200. Exit program")
    # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it
    print("")

    choice = int(input("Please select an option (n): "))

    if choice == 1:
        loan()

    elif choice == 2:
        return_book()

    elif choice == 3:
        extend_loan()

    elif choice == 4:
        search()

    elif choice == 200:
        quit()

    else:
        print("Your choice was invalid please try again")

def loan():
    print("loan books")

def return_book():
    print("return books")

def extend_loan():
    print("extend loan period")

def search():
    print("search")

# this is a secure way of calling main
if __name__ == '__main__':
    main()
