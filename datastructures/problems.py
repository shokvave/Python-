class LinkedList: 


# que -  write a python program to find maximum value in a linked list and replace it with given value

 def replace_max(self,value):
     temp = self.head
     max = temp

     while temp != None:
        if temp.data >max.data:
            max = temp
            temp = temp.next

     max.data = value

# que- write a python program to sum up the values at odd positons in a given linked list


 def sum_odd_nodes(self):
     temp = self.head
     counter = 0 
     while temp != None:
        if counter %2 == 0:
            result = result + temp.data
        counter+=1
        temp = temp.next


 def change_sent(self):
     temp = self.head

     while temp != None:
        if temp.data == '*' or temp.data == '/':
           temp.data = ' '

           if temp.data == '*' or temp.data == '/':
              temp.next.next.data = temp.next.next.data.upper()
              temp.next = temp.next.next

        temp = temp.next











