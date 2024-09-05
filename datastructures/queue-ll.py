class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self,value):
        self.front = None
        self.rear = None

    def enquque(self,value):
        
        new_node = Node(value)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    def dequeue(self):
        
        if self.front == None:
            return "Empty"
        else:
            self.front = self.front.next

    def isempty(self):
        if self.front == None:
            return "yes, Empty"
        

    def size (self):
        temp = self.front
        counter = 0

        while temp != None:
            counter+=1
            temp = temp.next

            return counter 
        
    def front_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.front.data
        
    
    def rear_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.rear.data


    def traverse(self):
        temp = self.front

        while temp != None:
            print(temp.data, end = ' ')
            temp = temp.next
