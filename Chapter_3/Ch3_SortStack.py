class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        temp = Stack()
        if not self.is_empty():
            while not self.is_empty() and item < self.peek():
                temp.push(self.pop())
            self.items.append(item)
            while not temp.is_empty():
                self.push(temp.pop())
        else:
            self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self,index=-1):
        return self.items.pop(index)

    def is_empty(self):
        return len(self.items) == 0

