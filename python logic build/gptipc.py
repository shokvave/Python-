def main():
    print("This is a monthly payment loan calculator")
    print("")

    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the interest rate: "))  # Convert apr to float
    years = int(input("Enter the number of years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print(" THe monthly payment for this loan is  : %.2f "  %monthly_payment)

main()
