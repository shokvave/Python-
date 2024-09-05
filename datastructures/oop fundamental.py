# object oriented fundamentals

# string = "hello"
# print(string.upper())  these methods these diffrent operations the things we can do with objects are based on their class

class Dog:# method can be simply define as a function that goes into a class

    def __init__(self, name):
        self.name = name
        


    def add_one(self, x):
        return x + 1


    def bark(self): 
        print("bark")

d = Dog('Tom')
print(d.name)
'''d.bark()
print(d.add_one(45))'''




