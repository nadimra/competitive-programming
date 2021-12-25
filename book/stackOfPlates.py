class StackOfPlates:
    def __init__(self,stackSize):
        self.stackCollection = []
        self.stackSize = stackSize
        self.pointerCollection = []
        self.createStack()

    def push(self,data):
        currentStackPointer = self.getCurrentStackPointer()
        if(currentStackPointer==self.stackSize-1):
            print("This stack is full, creating a new one")
            self.createStack()
            self.setCurrentStackPointer(1) #appends 1
            currentStackPointer = self.getCurrentStackPointer()
            self.getCurrentStack()[currentStackPointer] = data
        else:
            self.setCurrentStackPointer(1) #appends 1
            currentStackPointer = self.getCurrentStackPointer()
            self.getCurrentStack()[currentStackPointer] = data

    def pop(self):
        currentStackPointer = self.getCurrentStackPointer()
        if(currentStackPointer == -1 and len(self.stackCollection)>1):
            self.removeStack()
            currentStackPointer = self.getCurrentStackPointer()
            self.getCurrentStack()[currentStackPointer] = None
            self.setCurrentStackPointer(-1)
            return
        elif(currentStackPointer == -1 and len(self.stackCollection)==1):
            print("Remaining stack is empty, cannot remove")
            return
        else:
            currentStackPointer = self.getCurrentStackPointer()
            self.getCurrentStack()[currentStackPointer] = None
            self.setCurrentStackPointer(-1)
        
    def popAt(self,stackNum):
        currentStackPointer = self.getSpecificStackPointer(stackNum)
        if(currentStackPointer == -1):
            print("Cannot remove at specific stack")
            return
        else:
            self.getSpecificStack(stackNum)[currentStackPointer] = None
            self.setSpecificStackPointer(stackNum,-1)

    def displayAll(self):
        for i in range(0,len(self.stackCollection)):
            print("Displaying Stack "+str(i))
            for e in self.stackCollection[i]:
                print(str(e),end=" ")
            print()
        

    def createStack(self):
        self.stackCollection.append([None]*self.stackSize)
        self.pointerCollection.append(-1)

    def removeStack(self):
        del self.stackCollection[-1]
        del self.pointerCollection[-1]

    def getCurrentStack(self):
        return self.stackCollection[-1]
    
    def getCurrentStackPointer(self):
        return self.pointerCollection[-1]

    def setCurrentStackPointer(self,add):
        self.pointerCollection[-1] += add 

    def getSpecificStackPointer(self,stackNum):
        return self.pointerCollection[stackNum-1]

    def setSpecificStackPointer(self,stackNum,add):
        self.pointerCollection[stackNum-1] += add 

    def getSpecificStack(self,stackNum):
        return self.stackCollection[stackNum-1]

    def removeSpecificStack(self,stackNum):
        del self.stackCollection[stackNum-1]
        del self.pointerCollection[stackNum-1]


stacks = StackOfPlates(3)
stacks.push(1)
stacks.push(2)
stacks.pop()
stacks.pop()
stacks.pop()
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)
stacks.push(6)
stacks.push(7)
stacks.popAt(2)
stacks.popAt(2)
stacks.popAt(2)

stacks.displayAll()