import stack

def sortStack(s1,s2):
    while not s1.isempty():
        tempVar = s1.pop()
        placed = False
        while not placed:
            if s2.peek() is None or s2.peek()>tempVar:
                s2.push(tempVar)
                placed = True
            else:
                s1.push(s2.pop())

    s2.display()



s1 = stack.Stack()
s2 = stack.Stack()

s1.push(1)
s1.push(5)
s1.push(2)
s1.push(3)
s1.push(7)
s1.display()
print()
sortStack(s1,s2)