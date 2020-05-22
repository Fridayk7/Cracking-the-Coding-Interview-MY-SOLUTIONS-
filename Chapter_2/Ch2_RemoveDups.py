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

    def remove_dups(self):
        node = self.head
        dic = {}
        while node is not None:
            if dic.get(node.data) is not None:
                previous.next = node.next
            else:
                dic[node.data] = 1
                previous = node
            node = node.next

    def remove_dups2(self):
        node = self.head
        while node is not None:
            runner = node
            while runner.next is not None:
                if runner.next.data == node.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            node = node.next


