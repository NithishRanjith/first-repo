class a:
    def __init__(self):
        print("Constructor A")

    def a(self):
        print("Class A")


class B:
    def display(self):
        print("Class B")

    def __init__(self):

        super().__init__()
        print("Contructor B")


class C(B, a):
    def display(self):
        print("Class C")

    def __init__(self):

        super().__init__()
        print("Constructor C")


ob1 = B()
