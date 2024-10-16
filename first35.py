def N(a,b):
    if a>b :
        print("A is bigg :",a)
    
    else :
        print("B is bigg :",b)

N(10,34)
N(a= int(input("Enter the any no :")),b= int(input("Enter the any no :")))
print()

def bigg(a,b,c):
    if a>b and b>c :
        print("A is bigg :",a)
    elif b>c :
        print("B is bigg :",b)

    else :
        print("C is bigg :",c)


bigg(45,23,60)
bigg(a = int(input("enter the any no :")),
     b = int(input("Enter the any no :")),
     c = int(input("Enter the any no :")))