from array import *

A = array ('i',[2,3,4,5,6,7,8,9])
print(A)
print()

B = A
print(B)
print()

C = array(A.typecode,[i*2 for i in A])
print(C)
print()


D = array("i",[])
n = int(input("enter length of the array :"))

for i in range(n):
    X = int(input("Enter the value :"))

D.append(X)
print(D)
