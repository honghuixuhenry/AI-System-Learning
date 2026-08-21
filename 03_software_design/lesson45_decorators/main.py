def logger(func):
    def warpper():
        print("Start")
        func()
        print("End")
    return warpper

@logger
def hello():
    print("Hello")

hello()

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return result
    return wrapper