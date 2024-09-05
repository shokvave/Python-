#ask the user if they want to generate a passwd
#if yes ask for the passwd length
#Generate passwd
#print passwd
# if no then exit
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&*^")

def generate_passwd():
    passwd_length = int(input("enter preferable passwd lenght: "))

    random.shuffle(characters)

    passwd = []

    for x in range(passwd_length):
        passwd.append(random.choice(characters))

    random.shuffle(passwd)

    passwd = "".join(passwd)

    print(passwd)

while True:
    option = input("Do you want to generate a password? (yes/no): ").lower()

    if option == "yes":
        generate_passwd()
    elif option == "no":
        print("Program ended")
        break
    else:
        print("Invalid input, please enter 'yes' or 'no'.")


