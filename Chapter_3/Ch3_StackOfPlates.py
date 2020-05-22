class Stack:
    def __init__(self):
        self.capacity = 10
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self,index=-1):
        return self.items.pop(index)

    def is_full(self):
        return len(self.items) == self.capacity

    def is_empty(self):
        return len(self.items) == 0


class SetOfStacks:
    def __init__(self):
        self.stacks = [Stack()]

    def push(self, item):
        if self.stacks[-1].is_full():
            stack = Stack()
            stack.push(item)
            self.stacks.append(stack)
        else:
            self.stacks[-1].push(item)

    def pop(self):
        if self.stacks[-1].is_empty() and self.stacks[-1] != self.stacks[0]:
            self.stacks.pop(-1)
        elif self.stacks[0].is_empty():
            return "Nothing to pop"

        return self.stacks[-1].pop()

    def pop_at(self, index):
        n = self.stacks[index].pop()
        for i in range(index+1,len(self.stacks)):
            first = self.stacks[i].pop(0)
            self.stacks[i-1].push(first)
        return n

