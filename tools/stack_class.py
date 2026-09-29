class Stack:
    """Stack class"""
    # Constructor
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        if self.is_empty():
            return 0
        else:
            return len(self.items)








