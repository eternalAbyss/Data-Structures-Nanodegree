class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.data = dict({})
        self.order = []
        self.capacity = capacity
        self.length = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.data:
            return self.data[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.length < 10:
            self.data[key] = value
            self.length += 1
            self.order.append(key)
        elif key not in self.data:
            self.data.pop(self.order.pop(0))
            self.data[key] = value
            self.order.append(key)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)


print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2

our_cache.set(7, 7)
our_cache.set(8, 8)
our_cache.set(9, 9)
our_cache.set(10, 10)
our_cache.set(11, 11)
our_cache.set(12, 12)

print(our_cache.get(19))  # returns -1 because 19 is not present in the cache
print(our_cache.get(12))  # returns 12

our_cache.set(15, 15)
our_cache.set(6, 6)

print(our_cache.get(9)) # returns 9
