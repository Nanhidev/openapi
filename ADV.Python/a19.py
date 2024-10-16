class A:
    def F1(self):
        print("F1 function of class A !")

    
class B(A):
    def F2(self):
        print("F2 function of class B !")

class C(B):
    def F3(self):
        print("F3 function of class C !")

c = C()
c.F1()
c.F2()
c.F3()