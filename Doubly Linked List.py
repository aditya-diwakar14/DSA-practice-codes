class DNode:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DNode(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

obj = DLL()
obj.insert(100)
obj.insert(200)
obj.display()