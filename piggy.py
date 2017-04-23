class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.count + v <= self.capacity

    def add(self, v):
        self.count += v
