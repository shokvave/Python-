def main():
    print("this converts usd to pounds sterling")
    print()

    dollar = eval(input("enter amount in dollar: "))

    pounds = convert_to_pounds(dollar)

    print("that is", pounds,"pounds.")

convert_to_pounds = lambda dollar: dollar * 0.82 

main()
