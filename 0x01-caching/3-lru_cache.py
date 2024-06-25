#!/usr/bin/env python3
""" LIFO caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving items from a dictionary with LIFO mechanis.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.cache_lines = OrderedDict()
        self.line = 0
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_lines[key] = self.line
        self.line += 1
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)
        if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
            k = sorted(self.cache_lines, key=lambda x: self.cache_lines[x])[0]
            self.cache_data.pop(k)
            self.cache_lines.pop(k)
            print("DISCARD: {}".format(k))
        
    def get(self, key):
        """ Get an item in cache by key
        """
        if key is not None and key in self.cache_data:
            self.cache_lines[key] = self.line
            self.line += 1
        return self.cache_data.get(key, None)
