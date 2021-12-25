import stack

# 4
# 3 - 2 - 1

class MyQueue:
    def __init__(self):
        self.newStack = stack.Stack()
        self.oldStack = stack.Stack()
    
    def enqueue(self,data):
        self.newStack.push(data)
        print("Adding data to queue: "+str(data))

    def dequeue(self):
        if self.oldStack.isempty():
            if self.newStack.isempty():
                print("No items in queue to pop")
                return None
            else:
                while not self.newStack.isempty():
                    nodeData = self.newStack.pop()
                    self.oldStack.push(nodeData)
                print("Popping "+str(self.oldStack.peek()))
                return str(self.oldStack.pop())
        else:
                print("Popping "+str(self.oldStack.peek()))
                return str(self.oldStack.pop())
    
queue = MyQueue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.enqueue("d")
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()