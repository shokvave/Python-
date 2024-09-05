'''age = 20 
price = 18.23
first_name = 'Marsh'
is_online = False
print(age) 

name = input('What is your name??')
print("Hello " + name) 

birth_year = input("Enter your birth year;")
age = 2023 - int(birth_year)
print(age)

number_1 = input('Enter the first number: ')
number_2 = input('Enter the second number; ')

sum =  int(number_1) + int(number_2)

print('Sum: ' + str(sum)) 

temprature = 24

if temprature > 30 :
    print("It is a hot day")
    print("drink a lot of water")
elif temprature > 20:
    print('its a nice day')

print('done') 

weight = int(input("Weight: "))
unit = input('(K)g or (L)bs')

if unit.upper() == "K":
    converted = weight / 0.45
    print('Weight in lbs: ' + str(converted)  )
else:
    converted = weight * 0.45
    print('Weight in kgs: ' + str(converted)  )

i = 1 
while i <= 10:
    print(i * '*')
    i = i + 1 ''' 

numbers = range(5, 10, 2)
print(numbers)
for number in numbers:
    print(number)































