
# in this program well try to add a function that takes input from user in terms of year
# then tell is a leap year / is not a leap year
# put a while true so that program is repeated 
# also would have to define a fn or logic so that if user enters "exit" program ends
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
            else:
                print("Not leap year")
        else:
            print("leap year")
    else:
        print("Not lear year")


while True:
    user_input = input("enter a year(or type 'exit' to quit):")

    if user_input.lower() == "exit":
        print("program terminated.")
        break

    year = int(user_input)
    is_leap_year(year)