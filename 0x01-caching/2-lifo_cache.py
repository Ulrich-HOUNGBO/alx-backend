#!/usr/bin/env python3

"""
LIFO Caching
"""
from collections import deque

BaseCache = __import__("base_caching").BaseCaching


class LIFOCache(BaseCache):
    """Init"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)

    def is_full(self):
        """If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """you must print DISCARD: with the key discarded and following by a
        new line
        """
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
