name = "Honghui"
print(id(name))

a = 100
b = a
print(id(a))
print(id(b))

a = [1,2,3]
b = a
print(id(a))
b.append(4)
print(a)
print(b)
