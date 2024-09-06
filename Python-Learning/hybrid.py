# Hybrid - combination of mutlilevel, single and hierarchy
class dad:
    def phone(self):
        print("dad's phone")


class land:
    def important(self):
        print("important")


class son1(dad):
    pass


class son2(dad):
    pass


class son3(dad):
    pass


s2 = son2()
s2.phone()
