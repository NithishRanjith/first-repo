class grandpa:
    def phone(self):
        print("Grandpa phone")


class dad(grandpa):
    def money(self):
        print("Money from dad")


class son(dad):
    def laptop(self):
        print("sons'laptop")


ram = son()
ram.laptop()
ram.money()
ram.phone()

d1 = dad()
d1.phone()
