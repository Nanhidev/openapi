class A:
    def f1(self):
        print("f1 function of class method A !")


class B:
    def f1(self):
        print('f1 function of class method B !')

class C(A,B):
    def f3(self):
        B.f1(self)
        print('f3 function of class method C !')

class D(C):
    def f4(self):
        print('f4 function of class method D !')
        

class E(C):
    def f5(self):
        print('f5 function of class method E !')

e = E()
e.f1()
e.f3()

e.f5()
print()
print()

d = D()
d.f1()
d.f3()
d.f4()