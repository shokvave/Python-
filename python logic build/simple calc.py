#define the functions add sub mul dv
#print option to the user
#ask for value inputs
#call the functions
#while loop to continue the program until user wants to exit
def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + '=' + str(answer) )

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + '=' + str(answer) )

def mul(a, b):
    answer = a*b
    print(str(a) + "*" + str(b) + '=' + str(answer) )
    
def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + '=' + str(answer) )


print("A. addision")
print("S. substraction")
print("M. multiplication")
print("D. division")

print("E . exit")

choice = input("input your choice")
if choice == "a" or "A":
    print("Addition")
    a = int(input("input first number"))
    b = int(input("input second number"))
    add(a, b)
elif choice == "b" or "B":
    print("substraction")
    a = int(input("input first number"))
    b = int(input("input second number"))
    sub(a, b)
elif choice == "c" or "C":
    print("multiplication")
    a = int(input("input first number"))
    b = int(input("input second number"))
    mul(a, b)
elif choice == "d" or "D":
    print("division")
    a = int(input("input first number"))
    b = int(input("input second number"))
    div(a, b)
elif choice == "e" or "E":
    print("program ended")
    quit()