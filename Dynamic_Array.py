class DynamicArray:
    def __init__(self):
        self.data = []
        self.capacity = 1

    def append(self, val):
        if len(self.data) == self.capacity:
            print(f"Resize: Capacity {self.capacity} -> {self.capacity * 2}")
            self.capacity *= 2
        self.data.append(val)
        self.status()

    def pop(self):
        if self.data:
            self.data.pop()
            self.status()
        else:
            print("Underflow")

    def status(self):
        print(f"Size: {len(self.data)} | Capacity: {self.capacity} | Array: {self.data}")


da = DynamicArray()
da.append(10)
da.append(20)
da.append(30) 
da.pop()