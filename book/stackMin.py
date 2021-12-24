import stack 

currentStack = stack.Stack()
print("Empty: "+str(currentStack.isempty()))
currentStack.push(1)
currentStack.push(2)
currentStack.returnMin()
currentStack.push(0)
currentStack.returnMin()
currentStack.pop()
currentStack.returnMin()
currentStack.pop()
currentStack.returnMin()
currentStack.pop()
currentStack.returnMin()

