class parent:
    def f1(self):
        print("Parent Class Method !")
    
class Child(parent):
        def f2(self):
            print("Child Class Method !")

class Child1(Child):
        def f3(self):
            print("Child1 Class Method !")


c = Child1()
c.f1()
c.f2()
c.f3()
