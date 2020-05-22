class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = Node()

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()

def partition(head,k):
    small = SLinkedList()
    shead = small.head
    big = SLinkedList()
    bhead = big.head
    node = head
    while node is not None:
        if node.data < k:
            shead.next = Node(node.data)
            shead = shead.next
        else:
            bhead.next = Node(node.data)
            bhead = bhead.next
        node = node.next
    small.head = small.head.next
    big.head = big.head.next
    shead.next = big.head
    return small

