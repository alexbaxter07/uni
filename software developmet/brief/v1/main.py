import os
import csv
from datetime import datetime, timedelta

def main():

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
            choice = int(input("Please select an option (n): "))
        except ValueError:
            print("Please enter a number.")
            continue

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

        #the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later it also checks if its a number
        try:
            choice = int(input("Please select an option (n): "))
        except ValueError:
            print("Please enter a number.")
            continue

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
        print("### 5. Add new Book")
        print("### 6. Update Book Status")
        print("### 7. Change Staff Account Status")
        print("### 200. Exit program")
        # i choose 200 for this as if it was a single number there would be more chance of a user accidentally pressing it
        print("")

        #the function int will turn the users input to an integer as an input is always taken as a string this is easier for comparison later it also checks if its a number
        try:
            choice = int(input("Please select an option (n): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            loan()

        elif choice == 2:
            return_book()

        elif choice == 3:
            extend_loan()

        elif choice == 4:
            search()

        elif choice == 5:
            add_new()

        elif choice == 6:
            update_book()

        elif choice == 7:
            update_staff()

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

            break

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

    book_id = input("Please enter the book ID: ").strip()

    loaned_file = os.path.join(os.path.dirname(__file__), 'loaned.csv')
    books_file = os.path.join(os.path.dirname(__file__), 'inventories.csv')

    loans = []
    found = False

    # remove from loaned.csv
    with open(loaned_file, newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["BookID"] == book_id:

                found = True
                print("Book returned successfully")

            else:
                loans.append(row)

    if found == False:
        print("Book loan not found")
        return

    # save updated loaned.csv
    with open(loaned_file, "w", newline="") as f:

        fieldnames = ["BookID", "BorrowerID", "Due"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(loans)

    # update inventories.csv
    books = []

    with open(books_file, newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["BookID"] == book_id:
                row["CopiesAvailable"] = str(int(row["CopiesAvailable"]) + 1)

                row["OnLoan"] = str(int(row["OnLoan"]) - 1)

            books.append(row)

    # save updated inventories.csv
    with open(books_file, "w", newline="") as f:

        fieldnames = ["BookID", "Title", "Author", "Genre", "PublishedYear", "TotalCopies", "CopiesAvailable",
                      "OnLoan", "Deleted"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(books)

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

def add_new():

    books_file = os.path.join(os.path.dirname(__file__), 'inventories.csv')

    book_id = input("Please enter the new Book ID: ").strip()
    title = input("Please enter the book title: ").strip()
    author = input("Please enter the author: ").strip()
    genre = input("Please enter the genre: ").strip()
    published_year = input("Please enter the published year: ").strip()
    total_copies = input("Please enter the total number of copies: ").strip()

    books = []
    book_exists = False

    with open(books_file, newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["BookID"] == book_id:
                book_exists = True

            books.append(row)

    if book_exists == True:
        print("This Book ID already exists")
        return

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

    books.append(new_book)

    with open(books_file, "w", newline="") as f:

        fieldnames = ["BookID", "Title", "Author", "Genre", "PublishedYear", "TotalCopies", "CopiesAvailable", "OnLoan", "Deleted"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(books)

    print("New book added successfully")

def update_book():

    books_file = os.path.join(os.path.dirname(__file__), 'inventories.csv')

    book_id = input("Please enter the Book ID: ").strip()

    print("")
    print("Select new status")
    print("1. Available")
    print("2. On Loan")
    print("3. Deleted")

    choice = input("Enter choice: ").strip()

    books = []
    found = False

    with open(books_file, newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["BookID"] == book_id:

                found = True

                if choice == "1":

                    row["Deleted"] = "0"

                    if int(row["TotalCopies"]) > int(row["OnLoan"]):

                        row["CopiesAvailable"] = str(
                            int(row["TotalCopies"]) - int(row["OnLoan"])
                        )

                    print("Book status updated to Available")

                elif choice == "2":

                    row["OnLoan"] = row["TotalCopies"]
                    row["CopiesAvailable"] = "0"

                    print("Book status updated to On Loan")

                elif choice == "3":

                    row["Deleted"] = "1"

                    print("Book status updated to Deleted")

                else:
                    print("Invalid choice")
                    return

            books.append(row)

    if found == False:
        print("Book not found")
        return

    with open(books_file, "w", newline="") as f:

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

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(books)

def update_staff():

    staff_file = os.path.join(os.path.dirname(__file__), 'staff.csv')

    email = input("Please enter the staff email: ").strip()

    staff = []
    found = False

    with open(staff_file, newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["Email"] == email:

                found = True

                print("")
                print("Current status:", row["Status"])
                print("1. Active")
                print("2. Inactive")
                print("3. Blocked")

                choice = input("Please select the new status: ").strip()

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

            staff.append(row)

    if found == False:
        print("Staff account not found")
        return

    with open(staff_file, "w", newline="") as f:

        fieldnames = ["StaffID","Name","Email","Password","Role","Status","UserID","PhoneNumber","HireDate"
        ]

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(staff)

# this is a secure way of calling main
if __name__ == '__main__':
    main()
