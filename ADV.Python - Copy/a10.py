class outer:
    def __init__(self):
        print("outer class constructor")

    def f(self):
        print('outer the class method')

    class inner:
        def __init__(self):
            print("inner class constructor")

        def f1(self):
            print('inner the class method')


# a = outer()
# b = a.inner()
# b.f1()
# outer().inner().f1()
# b.f1()
# print()
# print()

o= outer()
o.f()
i = o.inner()
i.f1()