import linkedList as ll


# O(N)
def loopDetection(llist1):
    pointer1 = llist1.head
    occurances = {}
    while(pointer1 is not None):
        occurance = occurances.get(pointer1,False)
        if occurance:
            print("Loop starts at node "+str(pointer1.data))
            return True
        else:
            occurances[pointer1] = True
        pointer1 = pointer1.next

    return False


# Basic setup
llist1 = ll.LinkedList()

first_node = ll.Node(7)
second_node = ll.Node(1)
third_node = ll.Node(6)
fourth_node = ll.Node(6)
fifth_node = ll.Node(2)
sixth_node = ll.Node(3)
seventh_node = ll.Node(1)


llist1.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = third_node

print(loopDetection(llist1))