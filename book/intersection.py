import linkedList as ll

#O(N^2)
def intersection(llist1,llist2):
    pointer1 = llist1.head
    while(pointer1 is not None):
        pointer2 = llist2.head
        while(pointer2 is not None):
            if(pointer1==pointer2):
                return True
            pointer2 = pointer2.next
        pointer1 = pointer1.next
    return False

# O(N)
def intersectionOptimal(llist1,llist2):
    pointer1 = llist1.head
    occurances = {}
    while(pointer1 is not None):
        occurances[pointer1] = True
        pointer1 = pointer1.next
    
    pointer2 = llist2.head
    while(pointer2 is not None):
        occurance = occurances.get(pointer2,False)
        pointer2 = pointer2.next
        if occurance:
            return True

    return False




# Basic setup
llist1 = ll.LinkedList()
llist2 = ll.LinkedList()

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
fourth_node.next = fifth_node

llist2.head = sixth_node
sixth_node.next = third_node

print(llist1)
print(llist2)
print(intersection(llist1,llist2))
print(intersectionOptimal(llist1,llist2))