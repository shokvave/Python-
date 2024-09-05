class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None
    
    def push(self, value):

        new_node = Node(value)

        new_node.next = self.top

        self.top = new_node


    def peek(self):
        if(self.isempty()):
            return "Stack Empty"
        else:
            return self.top.data
        
    def pop(self):#not working properly giving the output "None"
        if(self.isempty()):
            return "Stack Empty"
        else:
            data = self.top.data
            self.top = self.top.next
            return data 

    def traverse(self):

        temp = self.top

        while temp != None:

            print(temp.data)
            temp = temp.next

def reverse_string(text): # this was a problem question called string reversal as name suggest
    s = Stack

    for i in text:
        s.push(i)#TypeError: Stack.push() missing 1 required positional argument: 'value' cant fix yet,, 

    res = " "

    while( not s.isempty()):
        res =   res + s.pop()

    print(res)

#reverse_string("hello")

#print(reverse_string)



def text_editor(text, pattern):
    u = Stack
    r = Stack

    for i in text:
        u.push(i)

    for i in pattern:

        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)
        res = ""

    while(not u.isempty()):
        res = u.pop() + res

    print(res)


text_editor("nigera","uuruur")

