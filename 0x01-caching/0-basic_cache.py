# /usr/bin/env python3

""" Basic dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class BasicCache"""

    def put(self, key, item):
        """Assign into dictionary"""
        if key and item:
            self.cache_data[key] = item
        return None

    def get(self, key):
        """Return value of cache_data linked to key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
