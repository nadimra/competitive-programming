import linkedList as ll

# a -> b -> c -> d

def kthToLast(llist,k):
    pointer1 = llist.head
    pointer2 = llist.head

    while k>0:
        #Todo: what happens when k is bigger?
        pointer2 = pointer2.next
        k-=1
        if(pointer2 is None):
            return
    
    while pointer2 is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1

# Basic setup
llist = ll.LinkedList()

first_node = ll.Node("a")
second_node = ll.Node("b")
third_node = ll.Node("c")
fourth_node = ll.Node("d")
fifth_node = ll.Node("e")
sixth_node = ll.Node("f")


llist.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
fifth_node.next = sixth_node

print(llist)
#removeDups(llist)
n = kthToLast(llist,7)
print(n.data)