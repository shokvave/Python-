

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
            else:
                print("Not lear year")
        else:
            print("leap year")
    else:
        print("Not lear year")

is_leap_year(2000)
 