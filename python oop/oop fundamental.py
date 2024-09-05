class Atm:
    # methods are basicaly a function written inside a clas
    def __init__(self) -> None:
        
        self.__pin = ""
        self.__balance = 0
           #constructor is a special method  jiske andar ka code automaticaly execute hota h jaise hi us class ka object bne 
        #  instance variable is a kind of a variable for which the value of variable is diffrent for diffrent objects
        
        self.menu()

    def menu(self):
        user_input = input("""
                      Hello how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit
        elif user_input == "3":
            self.withdraw
        elif user_input == "4":
            self.check_balance
        else:
            print("Bye")

    def create_pin(self):
        self.__pin = input("Enter your pin")
        print("Pin set succesfully")
    # if you are creating a class it will be a good practice to hide your data memeber with a "__"/"double undrscoere method" # nothing is truly private in python
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.__balance + amount
            print("Deposit succesfull")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.__balance:
                self.__balance - amount
                print("operationn succesfull")
            else:
                print("insufficient funds")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")



Sbi = Atm()
Sbi.deposit()















    
