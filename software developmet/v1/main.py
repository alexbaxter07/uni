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

    #double equals signs is a comparionsion which will return a boolean
    if choice == 1:
        staff_main_menu()

    elif choice == 2:
        stu_main_menu()

    elif choice == 200:
        quit()  # this function will stop the program

    else:
        print("Your choice was invalid please try again")

def staff_main_menu():

def stu_main_menu():
    while True:

        print("")
        print("####################################################")
        print("############## SHU Student Library management System ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total items sold by source")
        print("### 2. Total income by day")
        print("### 3. Total income from cash vs card")
        print("### 4. Income of cash over a period of time")
        print("### 5. Income of card over a period of time")
        print("### 6. Average income by source")
        print("### 7. Average income by day")
        print("### 8. Average income from cash vs card")
        print("### 9. Total Income by source")
        print("### 10. Total Income by source")

        choice = int(input("Please select an option (n): "))

        if choice == 1:
            source = tot_items_source()
            print("This is the total items sold by day:")
            print(source)
        elif choice == 2:
            day = income_day()
            print("This is the total income by day:")
            print(day)
            print("This shows the highest sales come from Friday.")
        elif choice == 3:
            cash_card = cash_vs_card()
            print("This is the total income of cash vs card:")
            print(cash_card)
            print("This shows most people prefer cash")
        elif choice == 4:
            cash_time = cash_period_of_time()
            print("This is the total income of cash over a period of time")
            print(cash_time)
        elif choice == 5:
            card_time = card_period_of_time()
            print("This is the total income of card over a period of time")
            print(card_time)
        elif choice == 6:
            av_source = av_income_source()
            print("This is the average income:")
            print(source)
        elif choice == 7:
            av_day = av_income_day()
            print("This is the average income by day:")
            print(av_day)
        elif choice == 8:
            av_cash_card = av_cash_vs_card()
            print("This is the average income of cash vs card:")
            print(av_cash_card)
        elif choice == 9:
            income_source = tot_income_source()
            print("Total income of each source: ")
            print(income_source)
            print("This shows highest sales come from the tickets")
        elif choice == 10:
            average_income_source = av_income_source()
            print("Average income of each source: ")
            print(average_income_source)
        elif choice == 200:
            quit()  # this function will stop the program
        else:
            print("Your choice was invalid please try again")

# this is a secure way of calling main
if __name__ == '__main__':
    main()
