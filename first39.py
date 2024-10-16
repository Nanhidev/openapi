a = 200

def N():
    a = 45
    print(a)
    print(globals()['a'])

def n():
    print(a)
N()
n()
print()

def A(a,b):
    print(a+b)

A(45,45)
print()


def F(a,b):
     print("Subtraction is :",a-b)

F(43,34)
F(50,30)
F(a = int(input("Enter the first no :")),
  b = int(input("Enter the Second no :")))