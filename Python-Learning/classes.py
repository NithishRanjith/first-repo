class goa:
    name = ""
    a = None

    def party(self):
        print("Partyyyyy")

    def beach(self):
        print("beacchhhhh")


r = goa()
s = goa()
r.party()
s.beach()
r.name = "ram"
r.gender = "M"
print(r.name)
print(r.gender)
s.name = "suresh"
print(s.name)
