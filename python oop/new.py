class Customer:
    def __init__(self, name) :
        self.name = name
        self.gender = gender


def greet(Customer):
    if Customer.gender == "Male":
     print("Hello",Customer.name,"Sir")
    else:
       print("Hello",Customer.name,"Maam")
       

cust = Customer("Nitish""Male")


greet(cust)