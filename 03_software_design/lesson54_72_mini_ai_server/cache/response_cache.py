# cache = {}

# def calculate(x):
#     if x in cache:
#         return cache[x]
#     result = x*x
#     cache[x] = result
#     return result

from functools import lru_cache
import time

# @lru_cache(maxsize=128)
# def calculate(x):
#     print("Calculating ... ")
#     time.sleep(3)
#     return x*x

# print(calculate(10))
# print(calculate(10))
# print(calculate(10))

# print(calculate.cache_info)

class ResponseCache:
    def __init__(self):
        self.cache = {}
    def get(self, key):
        return self.cache.get(key)
    def set(self, key, value):
        self.cache[key] = value
