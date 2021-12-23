import linkedList as ll


def removeDups(llist):
    occurancesMap = {}

    current = llist.head
    while current is not None:
        occurance =occurancesMap.get(current.data,False)
        if occurance==False:
            occurancesMap[current.data] = True
        else:
            #delete node
            llist.delete_node(llist,current)
        current = current.next
    
    print(llist)

def removeDupsMultiPointer(llist):
    pointer1 = llist.head

    while pointer1 is not None:
        pointer2 = pointer1.next
        while pointer2 is not None:
            if pointer2.data == pointer1.data:
                llist.delete_node(llist,pointer2)
            pointer2 = pointer2.next
        pointer1 = pointer1.next
    print(llist)

# Basic setup
llist = ll.LinkedList()

first_node = ll.Node("c")
second_node = ll.Node("c")
third_node = ll.Node("c")
fourth_node = ll.Node("c")

llist.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

print(llist)
#removeDups(llist)
removeDupsMultiPointer(llist)
