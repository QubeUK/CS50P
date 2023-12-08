class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity to few ")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Capacity exceeded")
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Nice try, but you cant have that many")
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
