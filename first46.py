def dbl(x):
    return x*2 

l = [2,3,4,5,6,7,8,9,10]
L = list(map(dbl,l))
print(L)
print()

print("Use Lambda Function !")
l = [4,3,2,5,6,7,8,9]
L = list(map(lambda x: x*5 , l))
print(L)
print()

L = [2,4,6,8,10,12,14,16]
L1 = [3,5,7,9,11,13,15,17]

List = list(map(lambda x,y : x+y, L , L1))
print(List)
print()

from functools import reduce 

def f(x,y):
    return x+y

L = [10,20,30,40,50,60,70,80,90] 

result = reduce(f,L)
print(result)
print()

print("lambda function !")
from functools import reduce
L = [10,20,30,40,50,60,70,80,90]
result = reduce(lambda x,y : x+y , L)
print(result)