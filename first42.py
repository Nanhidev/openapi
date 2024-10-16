def add(*args):
    s = 0
    for i in args:
        s = s+i
        print("Sum is :",s)

add(70,30)
print()
# add(12,24,36,48,60,72,84,96,108,120)
print()


def add(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k,'=',v)

add(a = 30, b = 40 , c = 50)
add(id=1 , name= 'Nanhi Deo',address= "Hyderabad",age=20,salary= 50000)
print()
print()

def f(a,b,/):
    print("Sum is :",a+b)

f(90,45)
print()

def F1(*,a,b):
    print('Sum is :',a+b)

F1(a =40, b=50)
F1(20,30)