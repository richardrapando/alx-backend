#!/usr/bin/python3

""" Basic Dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""

    def put(self, key, item):
        """Adds item in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves item from cache"""
        return self.cache_data.get(key, None)
