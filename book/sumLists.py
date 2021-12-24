import linkedList as ll

def linkedListValue(llist):
    pointer = llist.head
    accum = ""
    while pointer is not None:
        accum += str(pointer.data)
        pointer = pointer.next

    return int(accum)

def convertToLinkedList(val):
    newll = ll.LinkedList()
    for c in str(val):
        newll.append_node(newll,int(c))
    print(newll)

def sumLists(llistNode1,llistNode2,carry):
    if llistNode1 is None and llistNode2 is None and carry==0:
        return None
    
    value = carry
    if llistNode1 is not None:
        value += llistNode1.data
    if llistNode2 is not None:
        value += llistNode2.data

    newVal = value%10
    result = ll.Node(newVal)

    if(value>=10):
        newCarry=1
    else:
        newCarry=0


    result.next = sumLists(llistNode1.next if llistNode1 is not None else None,llistNode2.next if llistNode2 is not None else None,newCarry)

    return result


# Basic setup
llist1 = ll.LinkedList()
first_node1 = ll.Node(7)
second_node1 = ll.Node(1)
third_node1 = ll.Node(6)

llist2 = ll.LinkedList()
first_node2 = ll.Node(5)
second_node2 = ll.Node(9)

llist1.head = first_node1
first_node1.next = second_node1
second_node1.next = third_node1

llist2.head = first_node2
first_node2.next = second_node2
#second_node2.next = third_node2

#val1 = linkedListValue(llist1)
#val2 = linkedListValue(llist2)
#convertToLinkedList(val1+val2)

sum = sumLists(llist1.head,llist2.head,0)
summedList = ll.LinkedList()
summedList.head = sum
print(summedList)
