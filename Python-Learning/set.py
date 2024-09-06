# set - no duplicate values, can not modify the tuple but values can be added
# sets are unordered 
a = {1,2,4,1}
print(a)
a.add(6)
print(a)
a.remove(1)
print(a)
a.pop()
print(a)
a.pop()
print(a)