def A():         # this is lock variable
    a = 43
    print(a)

def B():
    b = 45
    print(b)
    
    
A()
B()

print()

# this is global variable

a = 500
def f():
    
    print(a)

def f1():
    print(a)

f()
f1()
print()


n = 5000
def N():
    global n
    print(n)

    n = 99
    print(n)

def N2():
    print(n)

N()
N2()


