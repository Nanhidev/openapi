class Test:
    a = 30

    def __init__(self):
        print('inside the constructor')
        print(self.a)
        print(Test.a)

    def m1(self):
        print('inside the method')
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print('inside the class method')
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print('inside the static method')
        print(Test.a)

S = Test()
S.m1()
S.m2()
S.m3()
print()
print()
print("Outside of the class !")
print(Test.a)
print(S.a)