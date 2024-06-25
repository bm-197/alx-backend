#!/usr/bin/env python3
""" FIFO caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict

class FIFOCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving items from a dictionary with FIFO mechanis.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
            print('DISCARD: {}'.format(self.cache_data.popitem(last=False)[0]))
        
        self.cache_data[key] = item
    
    def get(self, key):
        """ Get an item in cache by key
        """
        return self.cache_data.get(key, None)
