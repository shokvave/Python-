#collect the input : principal , apr, years
#calculate the monthly payment
# show the user

def main():
    print("This is monthly payment loan calculator")
    print("")

    pricipal = float(input("Enter the load amount: "))
    apr = input("Enter the interest rate: ")
    years = int(input("Enter the years"))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = pricipal * monthly_interest_rate / (1 -(1 + monthly_interest_rate) ** (-amount_of_months))

    print(" THe monthly payment for this loan is  : %.2f "  %monthly_payment)

main()