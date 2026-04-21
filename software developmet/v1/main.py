import os

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


def load_staff():
    staff = []

#error handling
     if not os.path.exists('staff.csv'):
       print("The staff file does not exist")
     return staff

    with open('staff.csv', "r") as f:

        lines = f.readlines()

        #STRIP HEADER
        for line in lines[1:]:

            data = line.strip().split(',')

            user ={
                "UserID": data[0],
                "Name": data[1],
                "Role": data[2],
                "Password": data[6],
                "Status": data[7],
            }

            staff.append(user)

    return staff

def find_user(staff,userid):

    for user in staff:
        if user["UserID"] == userid:
            return user

    return None

def save_staff(staff):

    with open('staff.csv', "w") as file:
        file.write("UserID,Name,Role,Status")

        for user in staff:
            line = f"{user["UserID"],user["Name"],user["Role"],user["Status"]}"
            file.write("UserID,Name,Role,Status")

def login():

    staff = load_staff()
    attempts = 0

    while attempts < 3:

        userid = input("Please input your userid: ").strip()
        password = input("Please input your password: ").strip()

        user = find_user(staff,userid)

        #uerid not found
        if user is None:
            attempts += 1
            print(f"Invalid userID, please try again. Attempts left: {3 - attempts}")

        elif user["Status"] != "active":
            print("your account is not active, cannot log in.")
            return None

        elif user["Password"] != password:
            attempts += 1
            print(f"Invalid password, please try again. Attempts left: {3 - attempts}")

            if attempts == 3:
                user["Status"] = "blocked"
                save_staff(staff)
                print("Your user has been blocked")

        else:
            print("Logged in successfully")
            return user

    return None

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
