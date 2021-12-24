import linkedList as ll

# 1 - 2 - 4 - 2 - 1
def reverseLinkedList(llist):
    pointer = llist.head
    rev_llist = ll.LinkedList()
    while pointer is not None:
        newNode = ll.Node(pointer.data)

        if rev_llist.head is not None:
            currentHead = rev_llist.head
            newNode.next = currentHead

        rev_llist.head = newNode
        pointer = pointer.next
    
    return rev_llist

def isPalindrome(llist, rev_llist):
    pointer1 = llist.head
    pointer2 = rev_llist.head

    while pointer1 is not None:
        if pointer1.data != pointer2.data:
            return False
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return True

# Basic setup
llist = ll.LinkedList()

first_node = ll.Node(1)
second_node = ll.Node(2)
third_node = ll.Node(4)
fourth_node = ll.Node(2)
fifth_node = ll.Node(1)


llist.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node

print(llist)
rev_llist = reverseLinkedList(llist)
print(rev_llist)

print(isPalindrome(llist,rev_llist))