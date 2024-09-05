class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1


    def push(self,value):
        if self.top == self.size - 1:
            return "Overflow"
        else:
            self.top+=1
            self.stack[self.top] = value
    
    def pop(self):

        if self.top == -1:
            return "Empty"
        else:
            data = self.stack [self.top]
            self.top-= 1
            print(data)

    def traverse(self):

        for i in range(self.top + 1 ):
            print(self.stack[i], end = " ")