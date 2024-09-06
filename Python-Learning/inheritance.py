class dad:
    def phone(self):
        print("Dads phone")


class mom:
    def sweet(self):
        print("sweet from mom")


class son(dad, mom):  # mutliple inheritance
    def laptop(self):
        print("son laptop")


ram = son()
ram.laptop()
ram.phone()
ram.sweet()
