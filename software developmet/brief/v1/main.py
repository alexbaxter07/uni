import os
# csv library is used to read and write csv files
import csv
# datetime is used for dates and timedelta is used to add days to dates
from datetime import datetime, timedelta

def main():

    # infinite loop keeps the menu running until the user exits
    while True:

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

        #the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later it also checks if its a number
        try:
            # stores the users menu choice
            choice = int(input("Please select an option (n): "))

        # ValueError happens if the user enters letters instead of a number
        except ValueError:
            print("Please enter a number.")
            # continue restarts the loop and shows the menu again
            continue

        #double equals signs is a comparison which will return a boolean
        if choice == 1:
            # calls the login function
            login()

        elif choice == 200:
            # this function will stop the program
            quit()

        else:
            print("Your choice was invalid please try again")

def login():

    # stores the amount of failed login attempts
    attempts = 0

    # creates the correct file path to staff.csv
    file_path = os.path.join(os.path.dirname(__file__), 'staff.csv')

    # loop continues until the user reaches 3 failed attempts
    while attempts < 3:

        # asks the user to enter their login details
        email = input("Please enter your email: ").strip()
        password = input("Please enter your password: ").strip()

        # opens the csv file in read mode
        with open(file_path, newline="") as f:

            # DictReader allows columns to be accessed by header names
            reader = csv.DictReader(f)

            # loops through every row in the csv file
            for row in reader:

                # checks if both the email and password match
                if row["Email"] == email and row["Password"] == password:

                    # checks if the account is active
                    if row["Status"] != "active":
                        print("Your account is not active.")
                        return

                    print("Login successful!")

                    # checks if the user is a librarian
                    if row["Role"] == "Librarian":
                        # opens the librarian menu
                        lib_main_menu()
                        return

                    # checks if the user is a supervisor
                    elif row["Role"] == "Supervisor":
                        # opens the supervisor menu
                        sup_main_menu()
                        return

            # adds 1 onto the attempts variable after a failed login
            attempts += 1
            print("Invalid email or password.")
            # shows the remaining attempts left
            print("Attempts left:", 3 - attempts)

    print("Too many failed attempts. Account should be blocked.")


def lib_main_menu():

    # infinite loop keeps the librarian menu running until the user exits
    while True:

        print("")
        print("####################################################")
        print("############## SHU Library management System ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Loan Books")
        print("### 2. Return Books")
        print("### 3. Extend loan period for Books")
        print("### 4. Search for Books")
        print("### 200. Exit program")

        # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it
        print("")

        #the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later it also checks if its a number
        try:
            # stores the users menu choice
            choice = int(input("Please select an option (n): "))

        # ValueError happens if the user enters letters instead of a number
        except ValueError:
            print("Please enter a number.")
            # continue restarts the loop and redisplays the menu
            continue

        # checks if the user selected loan books
        if choice == 1:
            # calls the loan function
            loan()

        # checks if the user selected return books
        elif choice == 2:
            # calls the return_book function
            return_book()

        # checks if the user selected extend loan
        elif choice == 3:
            # calls the extend_loan function
            extend_loan()

        # checks if the user selected search books
        elif choice == 4:
            # calls the search function
            search()

        # checks if the user selected exit
        elif choice == 200:
            # stops the program completely
            quit()

        else:
            print("Your choice was invalid please try again")


def sup_main_menu():

    # infinite loop keeps the supervisor menu running until the user exits
    while True:

        print("")
        print("####################################################")
        print("############## SHU Library management System ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Loan Books")
        print("### 2. Return Books")
        print("### 3. Extend loan period for Books")
        print("### 4. Search for Books")
        print("### 5. Add new Book")
        print("### 6. Update Book Status")
        print("### 7. Change Staff Account Status")
        print("### 200. Exit program")

        # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it
        print("")

        #the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later it also checks if its a number
        try:
            # stores the users menu choice
            choice = int(input("Please select an option (n): "))

        # ValueError happens if the user enters letters instead of a number
        except ValueError:
            print("Please enter a number.")
            # continue restarts the loop and redisplays the menu
            continue

        # checks if the user selected loan books
        if choice == 1:
            # calls the loan function
            loan()

        # checks if the user selected return books
        elif choice == 2:
            # calls the return_book function
            return_book()

        # checks if the user selected extend loan
        elif choice == 3:
            # calls the extend_loan function
            extend_loan()

        # checks if the user selected search books
        elif choice == 4:
            # calls the search function
            search()

        # checks if the user selected add new book
        elif choice == 5:
            # calls the add_new function
            add_new()

        # checks if the user selected update book status
        elif choice == 6:
            # calls the update_book function
            update_book()

        # checks if the user selected change staff account status
        elif choice == 7:
            # calls the update_staff function
            update_staff()

        # checks if the user selected exit
        elif choice == 200:
            # stops the program completely
            quit()

        else:

            print("Your choice was invalid please try again")

def load_books():

    # creates an empty list to store all of the books from the csv file
    books = []

    # creates the file path for inventories.csv
    file_path = os.path.join(os.path.dirname(__file__), 'inventories.csv')

    # opens the inventories.csv file in read mode
    with open(file_path, newline="") as f:

        # DictReader reads the csv file using the column headers
        reader = csv.DictReader(f)

        # loops through every row in the csv file
        for row in reader:

            # adds each book row into the books list
            books.append(row)

    # returns the completed list of books
    return books


def loan():

    # asks the user to enter the borrower ID and book ID
    borrower_id = input("Please enter the borrower's ID: ").strip()
    book_id = input("Please enter the book ID: ").strip()

    # boolean variables used to check if the borrower and book exist
    borrowers_found = False
    book_found = False

    # creates the file paths for the csv files needed in this function
    borrowers_file = os.path.join(os.path.dirname(__file__), 'borrowers.csv')
    books_file = os.path.join(os.path.dirname(__file__), 'inventories.csv')
    loaned_file = os.path.join(os.path.dirname(__file__), 'loaned.csv')

    # check borrower exists
    with open(borrowers_file, newline="") as f:

        # DictReader reads the borrower file using the column headers
        reader = csv.DictReader(f)

        # loops through every borrower in the file
        for row in reader:

            # checks if the borrower ID matches the one entered
            if row["BorrowerID"] == borrower_id:
                borrowers_found = True

    # checks if the borrower was not found
    if borrowers_found == False:
        print("Borrower not found")
        return

    # load books
    books = []

    # opens the inventories.csv file in read mode
    with open(books_file, newline="") as f:

        # DictReader reads the book file using the column headers
        reader = csv.DictReader(f)

        # loops through every book and adds it to the books list
        for row in reader:
            books.append(row)

    # search for book
    for book in books:

        # checks if the book ID matches the one entered
        if book["BookID"] == book_id:

            # changes book_found to True because the book exists
            book_found = True

            # update book numbers
            book["CopiesAvailable"] = str(int(book["CopiesAvailable"]) - 1)
            book["OnLoan"] = str(int(book["OnLoan"]) + 1)

            # create due date
            due_date = datetime.now() + timedelta(days=14)
            due_date = due_date.strftime("%d/%m/%Y")

            # add loan to loaned.csv
            with open(loaned_file, "a", newline="") as f:

                # sets the column headers for the loaned.csv file
                fieldnames = ["BookID", "BorrowerID", "Due"]
                # DictWriter allows dictionary data to be written to the csv file
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                # writes the new loan record into loaned.csv
                writer.writerow({
                    "BookID": book_id,
                    "BorrowerID": borrower_id,
                    "Due": due_date
                })

            print("Book loaned successfully")
            print("Due date:", due_date)

            # stops the loop once the correct book has been found
            break

    # checks if the book was not found
    if book_found == False:
        print("Book not found")
        return

    # save updated inventory
    with open(books_file, "w", newline="") as f:

        # sets the column headers for inventories.csv
        fieldnames = ["BookID", "Title", "Author", "Genre", "PublishedYear", "TotalCopies", "CopiesAvailable", "OnLoan", "Deleted"]
        # DictWriter is used to write the updated book list back into the file
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writes the headers back into the csv file
        writer.writeheader()
        # writes all updated book records back into inventories.csv
        writer.writerows(books)


def return_book():

    # asks the user to enter the ID of the book being returned
    book_id = input("Please enter the book ID: ").strip()

    # asks the user to enter the borrower ID
    borrower_id = input("Please enter the borrower ID: ").strip()

    # creates the file paths for loaned.csv and inventories.csv
    loaned_file = os.path.join(os.path.dirname(__file__), 'loaned.csv')
    books_file = os.path.join(os.path.dirname(__file__), 'inventories.csv')

    # creates an empty list to store loans that are not being removed
    loans = []

    # boolean variable used to check if the loan exists
    found = False

    # remove from loaned.csv
    with open(loaned_file, newline="") as f:

        # DictReader reads the loaned file using the column headers
        reader = csv.DictReader(f)

        # loops through every loan record
        for row in reader:

            # checks if both the book ID and borrower ID match
            if row["BookID"] == book_id and row["BorrowerID"] == borrower_id and found == False:
                found = True
                print("Book returned successfully")

            else:
                # keeps all other loans in the loans list
                loans.append(row)

    # checks if the loan was not found
    if found == False:
        print("Book loan not found")
        return

    # save updated loaned.csv
    with open(loaned_file, "w", newline="") as f:

        # sets the column headers for loaned.csv
        fieldnames = ["BookID", "BorrowerID", "Due"]

        # DictWriter writes the updated loans list back into the csv file
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # writes the headers back into the csv file
        writer.writeheader()

        # writes all remaining loans back into loaned.csv
        writer.writerows(loans)

    # update inventories.csv
    books = []

    # opens the inventories.csv file in read mode
    with open(books_file, newline="") as f:

        # DictReader reads the inventory file using the column headers
        reader = csv.DictReader(f)

        # loops through every book in the inventory
        for row in reader:

            # checks if the book matches the returned book
            if row["BookID"] == book_id:

                # adds 1 back to copies available
                row["CopiesAvailable"] = str(int(row["CopiesAvailable"]) + 1)

                # removes 1 from the number currently on loan
                row["OnLoan"] = str(int(row["OnLoan"]) - 1)

            # adds each book row to the books list
            books.append(row)

    # save updated inventories.csv
    with open(books_file, "w", newline="") as f:

        # sets the column headers for inventories.csv
        fieldnames = ["BookID","Title","Author","Genre","PublishedYear","TotalCopies","CopiesAvailable","OnLoan","Deleted"]

        # DictWriter writes the updated books list back into the csv file
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # writes the headers back into the csv file
        writer.writeheader()

        # writes all updated book records back into inventories.csv
        writer.writerows(books)
def extend_loan():

    # asks the user to enter the book ID for the loan they want to extend
    book_id = input("Please enter the book ID: ").strip()

    # creates the file path for loaned.csv
    loaned_file = os.path.join(os.path.dirname(__file__), 'loaned.csv')

    # creates an empty list to store all loan records
    loans = []

    # boolean variable used to check if the loan exists
    found = False

    # opens loaned.csv in read mode
    with open(loaned_file, newline="") as f:
        # DictReader reads the loaned file using the column headers
        reader = csv.DictReader(f)

        # loops through every loan record
        for row in reader:

            # checks if the loan matches the book ID entered
            if row["BookID"] == book_id:
                found = True

                # converts the due date string into a date object
                current_due = datetime.strptime(row["Due"], "%d/%m/%Y")
                # adds 14 days onto the current due date
                new_due = current_due + timedelta(days=14)
                # converts the new due date back into a string
                row["Due"] = new_due.strftime("%d/%m/%Y")

                print("Loan extended successfully")
                print("New due date:", row["Due"])

            # adds every row to the loans list
            loans.append(row)

    # checks if the loan was not found
    if found == False:
        print("Book loan not found")
        return

    # opens loaned.csv in write mode to overwrite it with updated data
    with open(loaned_file, "w", newline="") as f:

        # sets the column headers for loaned.csv
        fieldnames = ["BookID", "BorrowerID", "Due"]
        # DictWriter writes the updated loans back into the file
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writes the headers back into the csv file
        writer.writeheader()
        # writes all updated loan records back into loaned.csv
        writer.writerows(loans)

def search():

    # loads all books from inventories.csv using the load_books function
    books = load_books()

    # asks the user to enter a book ID or title and converts it to lowercase
    search_term = input("Please enter the book ID or title: ").strip().lower()

    # boolean variable used to check if a matching book is found
    found = False

    # loops through every book in the books list
    for book in books:

        # checks if the entered search term matches the book ID or title
        if book["BookID"].lower() == search_term or book["Title"].lower() == search_term:

            print("")
            print("Book found")
            print("Book ID:", book["BookID"])
            print("Title:", book["Title"])
            print("Author:", book["Author"])
            print("Copies Available:", book["CopiesAvailable"])
            print("On Loan:", book["OnLoan"])
            print("Deleted:", book["Deleted"])

            # changes found to True because a matching book was found
            found = True

    # checks if no matching book was found
    if found == False:
        print("Book not found")


def add_new():

    # creates the file path for inventories.csv
    books_file = os.path.join(os.path.dirname(__file__), 'inventories.csv')

    # asks the user to enter the details for the new book
    book_id = input("Please enter the new Book ID: ").strip()
    title = input("Please enter the book title: ").strip()
    author = input("Please enter the author: ").strip()
    genre = input("Please enter the genre: ").strip()
    published_year = input("Please enter the published year: ").strip()
    total_copies = input("Please enter the total number of copies: ").strip()

    # creates an empty list to store the current books
    books = []

    # boolean variable used to check if the book ID already exists
    book_exists = False

    # opens inventories.csv in read mode
    with open(books_file, newline="") as f:

        # DictReader reads the inventory file using the column headers
        reader = csv.DictReader(f)

        # loops through every book in the file
        for row in reader:

            # checks if the new book ID already exists
            if row["BookID"] == book_id:
                book_exists = True

            # adds each current book to the books list
            books.append(row)

    # checks if the book ID already exists
    if book_exists == True:
        print("This Book ID already exists")
        return

    # creates a dictionary for the new book record
    new_book = {
        "BookID": book_id,
        "Title": title,
        "Author": author,
        "Genre": genre,
        "PublishedYear": published_year,
        "TotalCopies": total_copies,
        "CopiesAvailable": total_copies,
        "OnLoan": "0",
        "Deleted": "0"
    }

    # adds the new book to the books list
    books.append(new_book)

    # opens inventories.csv in write mode to save the updated book list
    with open(books_file, "w", newline="") as f:

        # sets the column headers for inventories.csv
        fieldnames = ["BookID", "Title", "Author", "Genre", "PublishedYear", "TotalCopies", "CopiesAvailable", "OnLoan", "Deleted"]
        # DictWriter writes the updated books list back into the csv file
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writes the headers back into the csv file
        writer.writeheader()
        # writes all book records including the new one
        writer.writerows(books)

    print("New book added successfully")


def update_book():

    # creates the file path for inventories.csv
    books_file = os.path.join(os.path.dirname(__file__), 'inventories.csv')

    # asks the user to enter the book ID they want to update
    book_id = input("Please enter the Book ID: ").strip()

    print("")
    print("Select new status")
    print("1. Available")
    print("2. On Loan")
    print("3. Deleted")

    # asks the user to choose the new book status
    choice = input("Enter choice: ").strip()

    # creates an empty list to store all book records
    books = []

    # boolean variable used to check if the book exists
    found = False

    # opens inventories.csv in read mode
    with open(books_file, newline="") as f:
        # DictReader reads the inventory file using the column headers
        reader = csv.DictReader(f)

        # loops through every book in the file
        for row in reader:

            # checks if the book ID matches the one entered
            if row["BookID"] == book_id:

                found = True

                # checks if the user selected available
                if choice == "1":
                    # sets deleted to 0 so the book is not marked as deleted
                    row["Deleted"] = "0"

                    # checks if there are copies that are not currently on loan
                    if int(row["TotalCopies"]) > int(row["OnLoan"]):

                        # calculates how many copies should be available
                        row["CopiesAvailable"] = str(
                            int(row["TotalCopies"]) - int(row["OnLoan"])
                        )

                    print("Book status updated to Available")

                # checks if the user selected on loan
                elif choice == "2":

                    # sets all copies to on loan
                    row["OnLoan"] = row["TotalCopies"]

                    # sets available copies to 0
                    row["CopiesAvailable"] = "0"

                    print("Book status updated to On Loan")

                # checks if the user selected deleted
                elif choice == "3":

                    # marks the book as deleted
                    row["Deleted"] = "1"

                    # sets available copies to 0
                    row["CopiesAvailable"] = "0"

                    # sets books on loan to 0
                    row["OnLoan"] = "0"

                    print("Book status updated to Deleted")

                else:
                    print("Invalid choice")
                    return

            # adds each book row to the books list
            books.append(row)

    # checks if the book was not found
    if found == False:
        print("Book not found")
        return

    # opens inventories.csv in write mode to save the updated records
    with open(books_file, "w", newline="") as f:

        # sets the column headers for inventories.csv
        fieldnames = [
            "BookID",
            "Title",
            "Author",
            "Genre",
            "PublishedYear",
            "TotalCopies",
            "CopiesAvailable",
            "OnLoan",
            "Deleted"
        ]

        # DictWriter writes the updated book list back into the csv file
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # writes the headers back into the csv file
        writer.writeheader()

        # writes all updated book records back into inventories.csv
        writer.writerows(books)

def update_staff():

    # creates the file path for staff.csv
    staff_file = os.path.join(os.path.dirname(__file__), 'staff.csv')

    # asks the user to enter the email of the staff member
    email = input("Please enter the staff email: ").strip()

    # creates an empty list to store all staff records
    staff = []

    # boolean variable used to check if the staff member exists
    found = False

    # opens the csv file in read mode
    with open(staff_file, newline="") as f:

        # DictReader allows rows to be accessed using column names
        reader = csv.DictReader(f)

        # stores the column headers from the csv file
        fieldnames = reader.fieldnames

        # loops through every row in the csv file
        for row in reader:

            # checks if the email matches the entered email
            if row["Email"] == email:
                found = True

                print("")
                print("Current status:", row["Status"])
                print("1. Active")
                print("2. Inactive")
                print("3. Blocked")

                # asks the user to choose the new account status
                choice = input("Please select the new status: ").strip()

                # updates the status depending on the option chosen
                if choice == "1":
                    row["Status"] = "active"
                    print("Staff account changed to active")

                elif choice == "2":
                    row["Status"] = "inactive"
                    print("Staff account changed to inactive")

                elif choice == "3":
                    row["Status"] = "blocked"
                    print("Staff account changed to blocked")

                else:
                    print("Invalid choice")
                    return

            # appends every row into the list so the file can be rewritten later
            staff.append(row)

    # checks if the staff member was found
    if found == False:
        print("Staff account not found")
        return

    # opens the csv file in write mode to overwrite the old data
    with open(staff_file, "w", newline="") as f:

        # DictWriter writes dictionaries back into the csv file
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # rewrites the column headers
        writer.writeheader()
        # rewrites all updated rows back into the file
        writer.writerows(staff)

# this is a secure way of calling main
if __name__ == '__main__':
    main()
