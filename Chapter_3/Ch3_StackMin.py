class Stack:
    def __init__(self):
        self.items = []
        self.min_array = []

    def push(self, item):
        self.items.append(item)
        if self.min_array == []:
            self.min_array.append(item)
        elif item <= self.min_array[-1]:
            self.min_array.append(item)

    def pop(self):
        n = self.items.pop()
        if n == self.min_array[-1]:
            self.min_array.pop()
        return n

    def min(self):
        return self.min_array[-1]




