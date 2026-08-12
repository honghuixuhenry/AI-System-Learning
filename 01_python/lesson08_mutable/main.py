# a = 10
# b = a
# b = 20

# print(a)
# print(b)

# a = [10]

# b = a

# b[0] = 20

# print(a)
# print(b)

x = "AI"
print(id(x))

x = x + " System"
print(id(x))

numbers = [1, 2, 3]
print(id(numbers))
numbers.append(4)
print(id(numbers))

new_numbers = numbers
new_numbers.append(100)
print(numbers)
print(new_numbers)