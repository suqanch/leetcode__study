a = []
b = a
print(id(a))
print(id(b))
b.append(1)
print(id(a))
print(id(b))