# This program gets all applicable values from the user to calculate the cash-on-cash return-on-investment for a rental property.
# It utilizes imported (for brevity) helper functions to get income, expenses, initial investment amounts, and to calculate ROI, while displaying the current values and ROI percentage.
# The main program and helper functions utilize try-except blocks to ensure that a) invalid inputs do not crash the program, and b) valid data is preserved and returned.

from roi_helper_functions import get_income, get_expenses, get_investment, get_roi

def roi_calc():
    running = True
    total_income = 0
    total_expenses = 0
    initial_investment = 0
    while running == True:
        print('*'*50,"\n*   Welcome to the Cash-On-Cash ROI Calculator   *")
        print('*'*50,"\n")
        print(f"Current Cash-On-Cash ROI = {round(get_roi(total_income, total_expenses, initial_investment),2)}%\nCurrent Monthly Rental Income: ${total_income:,}\nCurrent Monthly Rental Expenses: ${total_expenses:,}\nCurrent Initial Investment: ${initial_investment:,}\n")
        print("Please enter all applicable data below using only numbers. Blank fields will default to 0.\n\nPLEASE CHOOSE:\n0) Quit\n1) Change Monthly Rental Income\n2) Change Monthly Rental Expenses\n3) Change Initial Investment\n4) Clear Current Values\n")
        try:    
            choice = int(input("CHOICE NUMBER: "))
            match choice:
                case 0:
                    running = False
                case 1:
                    total_income = get_income()
                case 2:
                    total_expenses = get_expenses()
                case 3:
                    initial_investment = get_investment()
                case 4:
                    total_income, total_expenses, initial_investment = 0,0,0
                case _:
                    input("I'm not even sure how you got to this line of code. It doesn't even need to exist really.")
        except:
            pass
        print("\n"*50)
    
roi_calc()
