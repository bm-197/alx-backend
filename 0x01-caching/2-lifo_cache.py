#!/usr/bin/env python3
""" LIFO caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict

class LIFOCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving items from a dictionary with LIFO mechanis.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)
        if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
            k = list(self.cache_data.keys())[-2]
            self.cache_data.pop(k)
            print('DISCARD: {}'.format(k))
        
    def get(self, key):
        """ Get an item in cache by key
        """
        return self.cache_data.get(key, None)
