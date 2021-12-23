import linkedList as ll

def deleteMiddleNode(llist):
    pointer1 = llist.head
    pointer2 = llist.head

    while pointer2.next is not None:
        if(pointer2.next.next is not None):
            pointer2 = pointer2.next.next
            pointer1 = pointer1.next
        else:
            pointer2 = pointer2.next
    
    llist.delete_node(llist,pointer1)

# Basic setup
llist = ll.LinkedList()

first_node = ll.Node("a")
second_node = ll.Node("b")
third_node = ll.Node("c")
fourth_node = ll.Node("d")
fifth_node = ll.Node("e")
#sixth_node = ll.Node("f")



llist.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node

print(llist)
deleteMiddleNode(llist)
print(llist)
