import linkedList as ll

# 2 - 4 - 1 - 5
def partition(llist,x):
    pointer = llist.head
    smaller = ll.LinkedList()
    bigger = ll.LinkedList()
    merged = ll.LinkedList()

    while pointer is not None:
        if(pointer.data >= x):
            bigger.append_node(bigger,pointer.data)
        else:
            smaller.append_node(smaller,pointer.data)
        pointer = pointer.next

    print(smaller)
    print(bigger)
    smallerLast = smaller.last_node(smaller)
    smallerLast.next = bigger.head
    merged.head = smaller.head
    print(merged)

# Basic setup
llist = ll.LinkedList()

first_node = ll.Node(1)
second_node = ll.Node(2)
third_node = ll.Node(4)
fourth_node = ll.Node(3)
fifth_node = ll.Node(2)
sixth_node = ll.Node(4)


llist.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
fifth_node.next = sixth_node

print(llist)
#removeDups(llist)
partition(llist,4)
