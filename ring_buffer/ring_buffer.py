class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [] # start with empty list
        self.oldestItem = 0 

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.oldestItem] = item
            if self.oldestItem < len(self.storage) - 1:
                self.oldestItem += 1
            else:
                self.oldestItem = 0

    def get(self):
        return self.storage