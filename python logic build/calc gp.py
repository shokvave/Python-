def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))
    
def div(a, b):
    if b != 0:
        answer = a / b
        print(str(a) + " / " + str(b) + " = " + str(answer))
    else:
        print("Error: Division by zero is not allowed.")


while True:

 print("A. Addition")
 print("S. Subtraction")
 print("M. Multiplication")
 print("D. Division")
 print("E. Exit") 

 choice = input("Input your choice: ").upper()

 if choice == "A":
    print("Addition")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    add(a, b)
 elif choice == "S":
    print("Subtraction")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    sub(a, b)
 elif choice == "M":
    print("Multiplication")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    mul(a, b)
 elif choice == "D":
    print("Division")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    div(a, b)
 elif choice == "E":
    print("Program ended.")
    quit()
 else:
    print("Invalid choice. Please choose A, S, M, D, or E.")



