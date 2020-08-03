class RingBuffer:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.storage = [None] * capacity
        self.head = 0

    def shift_idx(self, idx):
        return (idx + 1) % len(self.storage)

    def append(self, item):

        self.storage[self.head] = item
        self.head = self.shift_idx(self.head)

        if len(self.storage) > self.size:
            self.size += 1
            

    def get(self):
        return self.storage[:self.size]