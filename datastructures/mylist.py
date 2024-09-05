                                                                    #dynamic array and major logic 


import ctypes
 
class MeraList:

    def __init__(self) :
        self.size = 1
        self.n = 0
        # we have to create a c type array with size = self.size
        self.A = self._make_array(self.size)

    def __len__(self):
        return self.n 
    
    def __str__(self) -> str:
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return result
    
    def __getitem__(self,index):
        if 0<=index < self.n:
            return self.A[index]
        else:
            return 'IndexError'

    def __delitem__(self,pos):
        if 0<= pos < self.n:
         for i in range(pos,self.n-1):
            self.A[i] = self.A[i+1]

        self.n = self.n-1             
    
    def append(self,item):
        if self.n == self.size:

            self.__resize(self.size*2)


        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return 'Empty list'
        
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0 
        self.size = 1

    def find(self,item):

        for i in range(self.n):
            if self.A[i] == item:
                return i
            else:
                return 'ValueError  -  not in list'
            
    def insert(self,pos,item):
        if self.n ==  self.size:
            self.__resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n =self.n + 1

    def remove(self,item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

        

    def __resize(self,new_capacity):
        #create a new array with new capacity
        B = self.__make__array(new_capacity)
        self.size = new_capacity
        #copy the content of a to b
        for i in range(self.n):
            B[i] = self.A[i]
            #reassign a
            self.A = B

    def __make__array(self,capacity):
        #creates a c type array with size capacity
        return (capacity*ctypes.py_object)()
    
L = MeraList

L = ['10','50','60']
L.append("hello")
L.append(3.4) 
L.append(5685)
L.insert(3,99)

del L[2]

print(L)