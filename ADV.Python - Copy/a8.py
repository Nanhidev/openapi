class Student :
    inst = 'durgasoft were !'

    def __init__(self,m1,m2,m3) :
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        print(self.m1+self.m2+self.m3)

    @classmethod
    def m1(cls):
        print(cls.inst)

    @staticmethod
    def add(a,b):
        print('Sum is :',a+b)

    @staticmethod
    def f():
        print('Hello')


s = Student(90,80,70)
s.avg()
s.add(30,40)
s.f()
print()


s1 = Student(20,30,40)
s1.avg()
s1.add(600,500)
s1.f()