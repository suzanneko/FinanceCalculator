# This calculator will calculate the total amount of interest the user will receive on an investment or the monthly repayment required for a home loan.
# Asks user to select investment or bond to determine what is to be calculated.
# Program seeks to ensure input by user is recognised by stripping spaces and converting the input to lowercase.

import math
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n \ninvestment\t-\tto calculate the amount of interest you'll earn on your investment\nbond\t\t-\tto calculate the amount you'll have to pay on a home loan")
calc_type=input("\nEnter 'investment' or 'bond' to select the required calculator:")
calc_type=calc_type.lower()
calc_type=(calc_type.strip(" "))

# In the following section of code, if the user has entered 'investment', they are asked for the deposit size, interest rate, investment period and whether the interest is simple or compound.
# Using an if statement for whether the interest is simple or compounded, the program calculates the total amount the user will receive and prints it out.

if calc_type=="investment":
    deposit=float(input("Enter the amount of money that you are depositing in £:"))
    interest_rate=float(input("Enter the interest rate in %:"))
    num_years=float(input("Enter the number of years you plan on investing:"))
    interest=(input("Do you want simple or compound interest?:"))
    if interest=="simple":
        amount=deposit*(1+(interest_rate/100)*num_years)
    if interest=="compound":
        amount=deposit*math.pow(1+(interest_rate/100), num_years)
    print(f"\nThe total amount that you will receive at the end of the investment period is £{amount:.2f}.")
    print(f"\nThe interest that you'll earn on your investment is £{(amount-deposit):.2f}.")

# In the following section of code, if the user has entered 'bond', the program asks for the present value of the house, interest rate and repayment period.
# The program then calculates the monthly repayment that the user would have to make.

elif calc_type=="bond":
    present_value=float(input("Enter the present value of the house in £:"))
    interest_rate=float(input("Enter the interest rate in %:"))
    interest_rate=interest_rate/(100*12)
    num_months=float(input("Enter the number of months you plan to repay the home loan:"))
    amount=(present_value*interest_rate)/(1-((1+interest_rate)**(-1*num_months)))
    print(f"\lThe monthly repayment on the home loan will be £{amount:.2f}.")

else:
    print("You have not given a valid response. Please enter either 'bond' or 'investment'.")





