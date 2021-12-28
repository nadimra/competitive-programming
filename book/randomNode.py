import binaryTree
from random import randint

class BinarySearchNode():

    def __init__(self,value):
        self.size = 1
        self.left = None
        self.right = None
        self.value = value

    def append_node(self,value):
        if value > self.value:
            if(self.right is None):
                print("Add child right of "+str(self.value))
                self.right = BinarySearchNode(value)
            else:
                print("traverse right")
                self.right.append_node(value)
        else:
            if(self.left is None):
                print("Add child left of "+str(self.value))
                self.left = BinarySearchNode(value)
            else:
                print("traverse left")
                self.left.append_node(value)
        self.size +=1
    
    def find_node(self,value):
        if value == self.value:
            return self
        if value > self.value:
            if(self.right is None):
                print("Node does not exist")
                return None
            else:
                self.right.find_node(value)
        else:
            if(self.left is None):
                print("Node does not exist")
                return None
            else:
                self.left.find_node(value)

    def get_random(self):
        randNum = randint(1,self.size)
        if self.left is None:
            leftProbability = 0
        else:
            leftProbability = self.left.size
        
        if(randNum <= leftProbability):
            return self.left.get_random()
        elif(randNum == leftProbability+1):
            return self.value
        else:
            return self.right.get_random()


bTree = BinarySearchNode(10)
bTree.append_node(4)
bTree.append_node(11)
bTree.append_node(12)

print(bTree.get_random())