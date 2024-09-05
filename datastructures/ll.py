#linked list major functions and logic 
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

a = Node(1)
b = Node(2)
C = Node(3)

class Linkedlist:
    def __init__(self):
        #Empty linked List(ie. head = none)
        self.head = None
        #numbe of nodes in LL
        self.n = 0

    def __len__(self):
        #lenght of a linkedlist = number of nodes in the list
        return self.n
    
    def insert_head(self,value):
        #new node
        new_node = Node(value)
        #create connection
        new_node.next = self.head
        #reassign head
        self.head = new_node
        #increment n
        self.n = self.n + 1

    def __str__(self):
        curr =self.head
        
        result = ''

        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]
    
    def append(self,value):#insert middle
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1 
            return

        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node

    def insert_after(self,after,value):#insert tail
        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next


        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return 'item not found'


    def clear(self):
        self.head = None
        self.n = 0  

    def delete_head(self):

        if self.head == None:
            return 'Empty list'
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):
        if self.head == None:
            return 'Empty list'
        curr = self.head

        if curr.next == None:
             return self.delete_head()

        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.n = self.n - 1
    
    def remove(self,value):
        if self.head.data == value:
           return self.delete_head()
        
        if self.head == None:
            return 'Empty list'


        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

            if curr.next == None:
                return 'Not found'
            else:
                curr.next = curr.next.next
    def search(self,item):

        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return 'Not found'
    
    def __getitem__(self,index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return 'Index error'
            




L = Linkedlist()   

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.insert_head(5)






print(L.search(45))
