class Parent :
    def property(self):
        print('Cash+Gold+lands')

    def car(self):
        print('Alto car')
    

class Child(Parent):
    def car(self):
        super().car()
        print("Banz car")
c = Child()
c.property()
c.car()

print()


class Parent:
    def __init__(self):
        print("Parent Class Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Class Constructor !")

c = Child()