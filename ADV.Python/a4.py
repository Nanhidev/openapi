class test :
    def __init__(self):
        self.a = 30

    def m1(self):
        self.b = 50


s = test()
s.c = 90
s.m1()
print(s.__dict__)
print()


class Test :
    def __init__(self):
        self.a = 20
        self.b = 40


    def m1(self):
        print('withing the class')
        print(self.a)
        print(self.b)

t = Test()
t.m1()
print('outside of the class !')
print(t.a)
print(t.b)



