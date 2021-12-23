import linkedList as ll

def linkedListValue(llist):
    pointer = llist.head
    accum = ""
    while pointer is not None:
        accum += str(pointer.data)
        pointer = pointer.next

    return int(accum)


# Basic setup
llist1 = ll.LinkedList()
first_node1 = ll.Node(6)
second_node1 = ll.Node(1)
third_node1 = ll.Node(7)

llist2 = ll.LinkedList()
first_node2 = ll.Node(2)
second_node2 = ll.Node(9)
third_node2 = ll.Node(5)

llist1.head = first_node1
first_node1.next = second_node1
second_node1.next = third_node1

llist2.head = first_node2
first_node2.next = second_node2
second_node2.next = third_node2

val1 = linkedListValue(llist1)
val2 = linkedListValue(llist2)
print(val1+val2)
