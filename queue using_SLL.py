class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front: return "Underflow"
        val = self.front.data
        self.front = self.front.next
        if not self.front: self.rear = None
        return val

q = Queue()
q.enqueue("A")
q.enqueue("B")
print(f": {q.dequeue()}")