class Test1:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def m1(self):
        del self.a

a = Test1()
print(a.__dict__)

c = Test1()
print(c.__dict__)

a.m1()
del c.b
b = 100
print(a.__dict__)
print(c.__dict__)
print()



