a = {"name": "emc"}
print(a)
print(a["name"])
print(a.keys())
print(a.values())
a["age"] = 2
print(a)
a[1] = "age"
print(a)
a.update({"color": "yellow"})
print(a)
a.pop("age")
print(a)
a.clear()
print(a)