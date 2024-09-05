class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        if self.isempty():
            return "Stack Empty"
        else:
            return self.top.data
        
    def pop(self):
        if self.isempty():
            return None
        else:
            data = self.top.data
            self.top = self.top.next
            return data 

    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

def find_the_celeb(L):
    s = Stack()
    for i in range(len(L)):
        s.push(i)

    while not s.isempty():
        i = s.pop()
        j = s.pop()

        if j is None:
            celeb = i
            break

        if L[i][j] == 0:
            s.push(i)
        else:
            s.push(j)

    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print("No one is a celebrity")
                return

    print("The celebrity is",celeb) 

L = [
   [0,0,1,1],
   [0,1,0,0],
   [0,0,0,0],
   [0,0,1,0]
 ]          

find_the_celeb(L)


