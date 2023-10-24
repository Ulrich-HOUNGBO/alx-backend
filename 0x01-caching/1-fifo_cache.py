#!/usr/bin/env python3
""" FIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Class FIFOCache"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assign into dictionary using FIFO"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            elif len(self.cache_data) >= self.MAX_ITEMS:
                first = self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))
            self.queue.append(key)
        return None

    def get(self, key):
        """Return value of cache_data linked to key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
