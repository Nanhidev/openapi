class parent:
    def f1(self):
        print("parent class method !")

class Child(parent):
    def f2(self):
        print('Child class method !')

class Child2(Child):
    def f3(self):
        print("Child2 class parent !")

c = Child2()
c1 = Child()
c.f1()
c.f2()
c.f3()
print()

print(isinstance(c,Child2))
print(isinstance(c,Child))
print(isinstance(c,parent))
print()

print(isinstance(c1,Child2))
print(isinstance(c1,Child))
print(isinstance(c1,parent))
print()


print(issubclass(Child,parent))
print(issubclass(Child2,parent))
print(issubclass(Child,Child2))
print(issubclass(Child2,Child))
