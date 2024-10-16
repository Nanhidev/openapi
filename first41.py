def f(cource= "python"):
    print('Course is :',cource)

f("C++")
f()
f("Java")
print()
print()

def F2(Name , cource = "Django"):
    print(Name,"Course is :",cource)

F2("Shifa","Networking !")
F2("Nanhi","Full stack Python !")
F2("Kusum")
print()
print()

# variable length argument !
def f(*a):
    print(a)

f()
f(20,30)
f(45,67,56)
f(45,56,66,90)
print()

def add(*n):
    S = 0 
    for i in n:
        S = S+i
        print("Sum is :",S)

add(12,23)
print()
add(40,50,60,70,80)
print()
add(20,20,20,30,40,50)