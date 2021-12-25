#1 c2
#2 d1 - d2 - d3

from stack import Node
from enum import Enum


class Animal(Enum):
    DOG = "Dog"
    CAT = "Cat"

class NodeAnimal(Node):
    def __init__(self,data,animal):
        super().__init__(data)
        self.animal = animal

class QueueAnimal:
    def __init__(self):
        self.front = self.rear = None
 
    def isEmpty(self):
        return self.front == None
     
    # Method to add an item to the queue
    def enqueue(self, item, animal):
        temp = NodeAnimal(item,animal)
         
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
 
    # Method to remove an item from queue
    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
 
        if(self.front == None):
            self.rear = None
        return temp

    def display(self):
        iternode = self.front
        if self.isEmpty():
            print("Stack Underflow")
        else:
            while(iternode != None):
                print(str(iternode.data) + " ("+str(iternode.animal.value)+")","->",end = " ")
                iternode = iternode.next
            return

class AnimalShelter():
    def __init__(self,queue1,queue2):
        self.queue1 = queue1
        self.queue2 = queue2

    def enqueue(self,item,animal):
        if(self.queue1.isEmpty()):
            self.queue2.enqueue(item,animal)
        else:
            self.queue1.enqueue(item,animal)

    def dequeueAny(self):
        if(self.queue1.isEmpty() and self.queue2.isEmpty()):
            print("Queue is empty")
        elif self.queue1.isEmpty():
            self.queue2.dequeue()
        else:
            self.queue1.dequeue()

    def dequeueCat(self):
        if(self.queue1.isEmpty() and self.queue2.isEmpty()):
            print("Queue is empty")
        elif self.queue1.isEmpty():
            currentNode = self.queue2.dequeue()
            while currentNode.animal is not Animal.CAT:
                self.queue1.enqueue(currentNode.data,currentNode.animal)
                if not self.queue2.isEmpty():
                    currentNode = self.queue2.dequeue()
                else:
                    print("No cat exists")
                    return
            print("Dequeue "+str(currentNode.data))
            while not self.queue2.isEmpty():
                currentNode = self.queue2.dequeue()
                self.queue1.enqueue(currentNode.data,currentNode.animal)
        else:
            currentNode = self.queue1.dequeue()
            while currentNode.animal is not Animal.CAT:
                self.queue2.enqueue(currentNode.data,currentNode.animal)
                if not self.queue1.isEmpty():
                    currentNode = self.queue1.dequeue()
                else:
                    print("No cat exists")
                    return
            print("Dequeue "+str(currentNode.data))
            while not self.queue1.isEmpty():
                currentNode = self.queue1.dequeue()
                self.queue2.enqueue(currentNode.data,currentNode.animal)

    def dequeueDog(self):
        if(self.queue1.isEmpty() and self.queue2.isEmpty()):
            print("Queue is empty")
        elif self.queue1.isEmpty():
            currentNode = self.queue2.dequeue()
            while currentNode.animal is not Animal.DOG:
                self.queue1.enqueue(currentNode.data,currentNode.animal)
                if not self.queue2.isEmpty():
                    currentNode = self.queue2.dequeue()
                else:
                    print("No dog exists")
                    return
            print("Dequeue "+str(currentNode.data))
            while not self.queue2.isEmpty():
                currentNode = self.queue2.dequeue()
                self.queue1.enqueue(currentNode.data,currentNode.animal)
        else:
            currentNode = self.queue1.dequeue()
            while currentNode.animal is not Animal.DOG:
                self.queue2.enqueue(currentNode.data,currentNode.animal)
                if not self.queue1.isEmpty():
                    currentNode = self.queue1.dequeue()
                else:
                    print("No dog exists")
                    return
            print("Dequeue "+str(currentNode.data))
            while not self.queue1.isEmpty():
                currentNode = self.queue1.dequeue()
                self.queue2.enqueue(currentNode.data,currentNode.animal)

    def display(self):
        if(self.queue1.isEmpty() and self.queue2.isEmpty()):
            print("Queue is empty")
        elif self.queue1.isEmpty():
            self.queue2.display()
            print()
        else:
            self.queue1.display()
            print()

queue1 = QueueAnimal()
queue2 = QueueAnimal()





shelter = AnimalShelter(queue1,queue2)
shelter.display()
shelter.enqueue("kevin", Animal.DOG)
shelter.enqueue("chum", Animal.DOG)
shelter.enqueue("dodo", Animal.DOG)
shelter.enqueue("kitty", Animal.CAT)
shelter.enqueue("violet", Animal.CAT)
shelter.enqueue("jojo", Animal.DOG)
shelter.display()
shelter.dequeueAny()
shelter.display()
shelter.dequeueCat()
shelter.display()
shelter.dequeueCat()
shelter.display()
shelter.dequeueCat()
shelter.display()
shelter.dequeueCat()
shelter.dequeueDog()
shelter.display()
shelter.enqueue("kitty", Animal.CAT)
shelter.dequeueDog()
shelter.display()
shelter.dequeueCat()
shelter.display()
shelter.dequeueAny()
shelter.display()
shelter.dequeueAny()









