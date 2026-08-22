nums = [10,20,30]

for num in nums:
    print(num)

it = iter(nums)
while True:
    try:
        num = next(it)
        print(num)
    except StopIteration:
        break

def count():
    i = 0
    while True:
        yield i
        i += 1

c = count()
print(next(c))
print(next(c))
print(next(c))

def squares(n):
    for i in range(n):
        yield i*i
for num in squares(5):
    print(num)

def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a 
        a, b = b, a+b

for num in fibonacci(7):
    print(num)