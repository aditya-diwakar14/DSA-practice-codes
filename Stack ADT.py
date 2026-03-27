class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")
        
    def pop(self):
        if self.is_empty(): return "Underflow"
        return self.stack.pop()
        
    def peek(self):
        return self.stack[-1] if not self.is_empty() else "Empty"
        
    def is_empty(self):
        return len(self.stack) == 0

# Use Case: Undo Operation Simulation
undo_stack = Stack()
undo_stack.push("Type 'Hello'")
undo_stack.push("Type 'World'")
print(f"Undoing: {undo_stack.pop()}")