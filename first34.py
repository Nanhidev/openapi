def A():
    """Durga Soft Ware Solution !"""
a = A()
print(A.__doc__)
print()


def f():
    for i in range(10):
        print(i,"Hello")

f()
print()

def square(n):
    print("Square is :",n*n)

square(5)
square(15)
print()

def name(n):
    if n%2 == 0 :
        print("Even Number is :",n)
    
    else :
        print("Odd Number is :",n)

name(103)
name(n = int(input("Enter the any no :")))
