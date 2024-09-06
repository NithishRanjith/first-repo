# def add(a, b, c=10):
#     print(a + b + c)


# add(10, 20)
# add(10, 20, 34)


class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):  # Method overriding
        print("Dog barks")


d1 = Dog()
d1.sound()
