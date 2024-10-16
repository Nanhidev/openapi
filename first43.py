def F1():
    print("Hello")

F2 = F1
F2()
print(F2)
print(id(F2))
print(id(F1))
print()
print()

def F1():
    print("Hello")

    def F2():
        print("Haii")

        def F3():
            print("Welcome")

        F3()
    F2()
F1()

print()


def multi(a):
    def mul(b):
        def mu(c):
            return  a*b*c
        
        return mu
    return mul
y = multi(2)(2)(3)
print(y)
