# List - can have duplicate values, different data types
a = [1, 2, 3]
b = [6, 6]
print(type(a))
a.append("emc")

a.insert(0, "hello")
print(a)
a.pop(4)
print(a)
a.extend(b);
print(a)