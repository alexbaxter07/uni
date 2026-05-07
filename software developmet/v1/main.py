import os
import csv
import datetime, timedelta

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
    attempts = 0
    file_path = os.path.join(os.path.dirname(__file__), 'staff.csv')

    while attempts < 3:
        email = input("Please enter your email: ").strip()
        password = input("Please enter your password: ").strip()

        with open(file_path, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                if row["Email"] == email and row["Password"] == password:

                    if row["Status"] != "active":
                        print("Your account is not active.")
                        return

                    print("Login successful!")

                    if row["Role"] == "Librarian":
                        lib_main_menu()
                        return

                    elif row["Role"] == "Supervisor":
                        sup_main_menu()
                        return

            attempts += 1
            print("Invalid email or password.")
            print("Attempts left:", 3 - attempts)

    print("Too many failed attempts. Account should be blocked.")


def lib_main_menu():

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

def load_books():

    books = []
    file_path = os.path.join(os.path.dirname(__file__), 'inventories.csv')

    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            books.append(row)

    return books

def loan():

    borrower_id = input("Please enter the borrower's ID: ").strip()
    book_id = input("Please enter the book ID: ").strip()

    borrowers_found = False
    book_found = False

    borrowers_file = os.path.join(os.path.dirname(__file__), 'borrowers.csv')
    books_file = os.path.join(os.path.dirname(__file__), 'inventories.csv')
    loaned_file = os.path.join(os.path.dirname(__file__), 'loaned.csv')

    # check borrower exists
    with open(borrowers_file, newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["BorrowerID"] == borrower_id:
                borrowers_found = True

    if borrowers_found == False:
        print("Borrower not found")
        return

    # load books
    books = []

    with open(books_file, newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:
            books.append(row)

    # search for book
    for book in books:

        if book["BookID"] == book_id:

            book_found = True

            if book["Deleted"] == "1":
                print("Book has been deleted")
                return

            if int(book["CopiesAvailable"]) <= 0:
                print("No copies available")
                return

            # update book numbers
            book["CopiesAvailable"] = str(int(book["CopiesAvailable"]) - 1)
            book["OnLoan"] = str(int(book["OnLoan"]) + 1)

            # create due date
            due_date = datetime.now() + timedelta(days=14)
            due_date = due_date.strftime("%d/%m/%Y")

            # add loan to loaned.csv
            with open(loaned_file, "a", newline="") as f:

                fieldnames = ["BookID", "BorrowerID", "Due"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writerow({
                    "BookID": book_id,
                    "BorrowerID": borrower_id,
                    "Due": due_date
                })

            print("Book loaned successfully")
            print("Due date:", due_date)

    if book_found == False:
        print("Book not found")
        return

    # save updated inventory
    with open(books_file, "w", newline="") as f:

        fieldnames = ["BookID", "Title", "Author", "Genre", "PublishedYear", "TotalCopies", "CopiesAvailable", "OnLoan", "Deleted"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(books)

def return_book():
    print("return books")

def extend_loan():

    book_id = input("Please enter the book ID: ").strip()

    loaned_file = os.path.join(os.path.dirname(__file__), 'loaned.csv')

    loans = []
    found = False

    with open(loaned_file, newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["BookID"] == book_id:

                found = True

                current_due = datetime.strptime(row["Due"], "%d/%m/%Y")

                new_due = current_due + timedelta(days=14)

                row["Due"] = new_due.strftime("%d/%m/%Y")

                print("Loan extended successfully")
                print("New due date:", row["Due"])

            loans.append(row)

    if found == False:
        print("Book loan not found")
        return

    with open(loaned_file, "w", newline="") as f:

        fieldnames = ["BookID", "BorrowerID", "Due"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(loans)

def search():

    books = load_books()

    search_term = input("Please enter the book ID or title: ").strip().lower()

    found = False

    for book in books:

        if book["BookID"].lower() == search_term or book["Title"].lower() == search_term:

            print("")
            print("Book found")
            print("Book ID:", book["BookID"])
            print("Title:", book["Title"])
            print("Author:", book["Author"])
            print("Copies Available:", book["CopiesAvailable"])
            print("On Loan:", book["OnLoan"])
            print("Deleted:", book["Deleted"])

            found = True

    if found == False:
        print("Book not found")

# this is a secure way of calling main
if __name__ == '__main__':
    main()
