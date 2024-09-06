class phone:
    class_variable = "class"

    def __init__(self, brand, price):
        self.brand = brand  # instance variable
        self.price = price  # instance variable

    def display(self):
        print(self.brand)
        print(f"Price : {self.price}")
        print(self.class_variable)


phone.class_variable = "new_Class"
samsung = phone("Samsung", 2000)
samsung.display()
redmi = phone("redmi", 2000)
redmi.display()
