
class Node:
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self,data):
        self.data = data
        self.next = None
        self.nextMin = None
     
class Stack:
    # head is default NULL
    def __init__(self):
        self.head = None
        self.currentMin = None
     
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
     
    # Method to add data to the stack
    # adds to the start of the stack
    def push(self,data):
         
        if self.head == None:
            self.head=Node(data)
            self.currentMin = self.head
        else:                
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

            if(data<self.currentMin.data):
                newnode.nextMin = self.currentMin
                self.currentMin = newnode

     
    # Remove element that is the current head (start of the stack)
    def pop(self):
         
        if self.isempty():
            return None
             
        else:
            # Removes the head node and makes
            #the preceding one the new head

            poppednode = self.head
            if(self.currentMin == poppednode):
                self.currentMin = poppednode.nextMin
            self.head = self.head.next
            poppednode.next = None

            if(self.isempty()):
                self.currentMin = None
            return poppednode.data
     
    # Returns the head node data
    def peek(self):
         
        if self.isempty():
            return None
             
        else:
            return self.head.data
     
    # Prints out the stack    
    def display(self):
         
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
         
        else:
             
            while(iternode != None):
                 
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return
    
    def returnMin(self):
        if self.currentMin is not None:
            print("\nMin is: "+str(self.currentMin.data))
            return self.currentMin
        else:
            print("Stack empty")
            return
