import math

# First print the menu to the user
# Follow with an input for the user to enter their choice
print("1. Investment - to calculate the amount of interest you'll earn on your investment")
print("2. Bond - to calculate the amount you'll have to pay on your home loan")
# Use .lower() for the input so that no matter how the user inputs their response,
# the input will be changed to lower case and the input will not affect the code.
calc_choice = str(input(
    "Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()
# Create an if statement for if the entry is investment, even if spelled upper case,
# lower case or anything in between, it will not affect the code progressing.
if calc_choice == "investment":
    deposit = float(
        input("Please enter the amount of money you will deposit : "))
    interest_rate = float(input("Please input the interest rate : "))
    length_of_investment = int(
        input("Please enter the number of years you plan on investing : "))
    interest_type = str(input(
        "Please input whether you want 'simple' or 'compound' interest : ")).lower()
    # convert the interest rate to a decimal form
    interest_rate /= 100
    # take the above information, to work out the total amount based on the interest rate
    if interest_type == "simple":
        total_amount = deposit * (1 + interest_rate * length_of_investment)
    elif interest_type == "compound":
        total_amount = deposit * \
            math.pow((1 + interest_rate), length_of_investment)
    else:
        print("Interest type not found")
    # show the result using 'f' statement
    total_amount = round(total_amount, 2)
    print(
        f"The total amount returned on your investment after {length_of_investment} years on the {interest_type} interest is: {total_amount}")

# Now we create the elif statement for the event the user inputs 'bond'
elif calc_choice == "bond":
    house_value = float(input("What is the present value of the house? "))
    bond_interest_rate = float(
        input("What is the interest rate of your bond? "))
    bond_repayment = int(
        input("How many months will you repay the bond over? "))
    # Now convert the interest rate from yearly to a monthly rate
    bond_interest_rate = ((bond_interest_rate / 100) / 12)
    # Monthly payments to be calculated
    monthly_payment = round(((house_value * bond_interest_rate) / (1 - (1 + bond_interest_rate) ** (- bond_repayment))), 2)
    # print the result to the user using f statement
    print(f"The monthly bond payment is £{monthly_payment}")
else:
    print("Invalid choice. Please enter either 'investment' or 'bond'.")
