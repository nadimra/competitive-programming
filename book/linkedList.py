class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def delete_node(self,llist, selectedNode):
        n = llist.head
        if(selectedNode==llist.head):
            llist.head = selectedNode.next
        else:
            while n.next != None:
                if n.next == selectedNode:
                    n.next = n.next.next
                    break
                n = n.next
        return llist

        
