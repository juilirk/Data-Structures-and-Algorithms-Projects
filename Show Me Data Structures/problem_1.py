from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity=None):
        # Initialize class variables
        self.cache_memory = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            value = self.cache_memory.pop(key)
            self.cache_memory[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity == 0 or self.capacity is None:
            print("Capacity of our cache is zero or null!")
            return
        if key in self.cache_memory:
            # poping to update the priority in dictionary
            self.cache_memory.pop(key)
            self.cache_memory[key] = value
            return
        # if the cache memory is not full, then just add it
        if len(self.cache_memory) < self.capacity:
            self.cache_memory[key] = value
        else:
            # if full, then remove the least recently used item
            self.cache_memory.popitem(last=False)
            self.cache_memory[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))    # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))


our_cache = LRU_Cache(4)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(1, 4)
our_cache.set(4, 5)
our_cache.set(5, 6)
print(our_cache.get(1))  # should return 4
print(our_cache.get(2))  # should return -1 because it is least recently used


our_cache = LRU_Cache(0)
our_cache.set(1, 1)  # should print capacity of your cache is zero or null!
our_cache = LRU_Cache()
our_cache.set(1, 1)  # should print capacity of your cache is zero or null!
