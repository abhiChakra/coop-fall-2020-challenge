class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def add(self, num: int):
        self.undo_stack.push(-1 * num)
        self.value = self.value + num

    def subtract(self, num: int):
        self.undo_stack.push(num)
        self.value = self.value - num

    def undo(self):
        if self.undo_stack.isEmpty() is False:
            undo_val = self.undo_stack.pop()
            self.value = self.value + undo_val
            self.redo_stack.push(-1 * undo_val)

    def redo(self):
        if self.redo_stack.isEmpty() is False:
            redo_val = self.redo_stack.pop()
            self.value = self.value + redo_val
            self.undo_stack.push(-1 * redo_val)

    def bulk_undo(self, steps: int):
        for _ in range(steps):
            if self.undo_stack.isEmpty():
                break
            else:
                self.undo()

    def bulk_redo(self, steps: int):
        for _ in range(steps):
            if self.redo_stack.isEmpty():
                break
            else:
                self.redo()

class Stack():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, val : int):
        self.items.append(val)
    
    def pop(self):
        if self.isEmpty() is False:
            return self.items.pop()