S = lambda n:n*n
print(S(5))
print()

N = lambda a,b : a+b
print(N(45,60))
print()

N = lambda a,b :a if a>b else b
print(N(50,34))
print()

N = lambda a,b,c : a if a>b and a>c else b if b>c else c
print(N(40,20,45))
print()


N = lambda s: "even no !" if s%2 == 0 else "odd no !"
print(N(51))
print(N(24))
print()


n = 0
for i in range(1000):
    if i%3== 0 or i%5 == 0:
        n = n+i
print(n)
print()


def N(i):
    if i%2 != 0 :
        return True
    return False
L = [2,3,4,5,6,7,8,9,10,11]
L1 = list(filter(N,L))
print(L1)
print("lambda Function !")

L = [1,2,3,4,5,6,7,8,9,10,11,12]
L1 = list(filter(lambda x : x%2== 0 ,L ))
print(L1)