class MultiStackFixed:
    def __init__(self,stackSize,partitions):
        self.arraySize = stackSize
        self.partitions = partitions
        self.stacks = [None] * stackSize*partitions
        self.pointerLocations = [-1]*partitions

    def push(self,partitionNum,data):
        if(self.pointerLocations[partitionNum-1]==self.arraySize-1):
            print("Stack is full")
        else:
            startLocation = self.arraySize*(partitionNum-1)
            self.pointerLocations[partitionNum-1] += 1
            self.stacks[startLocation+self.pointerLocations[partitionNum-1]] = data

    def pop(self,partitionNum):
        if self.isEmpty(partitionNum):
            print("Stack is already empty")
        else:
            startLocation = self.arraySize*(partitionNum-1)
            self.stacks[startLocation+self.pointerLocations[partitionNum-1]] = None
            self.pointerLocations[partitionNum-1] -= 1


    def isEmpty(self,partitionNum):
        if self.pointerLocations[partitionNum-1] == -1:
            return True
        else:
            return False

    def displayStack(self,partitionNum):
        startLocation = self.arraySize*(partitionNum-1)
        endLocation = self.arraySize*(partitionNum-1) + self.arraySize
        print("Printing stack: "+str(partitionNum))
        for i in range(startLocation,endLocation):
            print(self.stacks[i],end =" ")
        print()

    def displayAll(self):
        print("Whole data")
        for i in range(0,len(self.stacks)):
            print(self.stacks[i],end =" ")
        print()


multiStack = MultiStackFixed(3,3)

multiStack.push(2,"D")
multiStack.push(2,"D")
multiStack.push(2,"D")
multiStack.push(2,"D")
multiStack.push(3,"B")
multiStack.push(3,"B")
multiStack.push(3,"B")
multiStack.push(3,"B")
multiStack.pop(3)
multiStack.pop(3)
multiStack.pop(3)
multiStack.pop(3)

multiStack.displayAll()

