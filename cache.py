import time
from collections import deque
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}
        self.lastUsed = []

    # @return an integer
    def get(self, key):
        if (key in self.data):
            self.lastUsed.append(key)
            return self.data[key]
        else:
            return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self.lastUsed.append(key)
        if key in self.data:
            self.data[key] = value
        else:
            if (len(self.data.keys()) == self.capacity):
                import pdb; pdb.set_trace()
                keyLastUsed = self.lastUsed.pop(0)
                while (keyLastUsed not in self.data):
                    keyLastUsed = self.lastUsed.pop(0)
                self.data.pop(keyLastUsed, None)
            self.data[key] = value

cache = LRUCache(2)
print [cache.set(2,1),cache.set(1,1),cache.get(2),cache.set(4,1),cache.get(1),cache.get(2)]