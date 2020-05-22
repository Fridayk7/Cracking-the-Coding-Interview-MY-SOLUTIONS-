class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()


def delete_middle(node):
    while node.next is not None:
        node.data = node.next.data
        node = node.next
    node.data = None

