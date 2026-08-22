import threading

def task():
    print("Running")

t = threading.Thread(target=task)

t.start()
t.join()

import time

def printA():
    for i in range(3):
        print("A")

def printB():
    for i in range(3):
        print("B")

t1 = threading.Thread(target=printA)
t2 = threading.Thread(target=printB)

t1.start()
t2.start()
t1.join()
t2.join()

import threading

count = 0

def task():
    global count
    for _ in range(100000):
        count += 1

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

print(count)