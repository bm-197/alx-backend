#!/usr/bin/env python3
""" LIFO caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict

class LFUCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving items from a dictionary with LIFO mechanis.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.cache_lines = OrderedDict()
        self.cache_freq = defaultdict(int)
        self.line = 0
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        self.cache_lines[key] = self.line
        self.cache_freq[key] += 1
        self.line += 1
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)
        if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
            freq_k = sorted(self.cache_freq, key=lambda x: self.cache_freq[x])
            lfu_k = freq_k[0]
            k = lfu_k
            i = 1
            while i < len(freq_k) and freq_k[i] <= lfu_k:
                if self.cache_lines[freq_k[i]] < self.cache_lines[lfu_k]:
                    k = freq_k[i]
                i += 1
            self.cache_data.pop(k)
            self.cache_lines.pop(k)
            self.cache_freq.pop(k)
            print("DISCARD: {}".format(k))
        
    def get(self, key):
        """ Get an item in cache by key
        """
        if key is not None and key in self.cache_data:
            self.cache_lines[key] = self.line
            self.cache_freq[key] += 1
            self.line += 1
        return self.cache_data.get(key, None)
my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()
