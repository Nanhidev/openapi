t = (23,'nanhi',54.45,None, "Mushkan")
print(t)

print(100 in t)     # false
print("nanhi" in t)           # True
print(100 not in t)     # True
print("nanhi" not in t)         # false
print()

tup = ("Mushkan",'aaush',534,435,5.34,None,"akku")
print(len(tup))

tup1 = (34,45,67,-1,45,23,49,90,-90,-8)
print(max(tup1))
print(min(tup1))
print(sum(tup1))
print(sum(tup1,4))
print()


t = "durgaSpft"
print(t)
print(type(t))
print(tuple(t))
print()

t2 = tuple(t)
print(type(t2))
print(t2)
print()

t = [23,45,67,87,98,34]
print(t)
print(type(t))
print(tuple(t))
print(set(t))
print()

t = 20,30,40
a, b, c = t
print(t)
print(type(t))
print()


t = (200,400,600,800)
print(t)

a ,b ,c = t
a = t
b = t
c = t
print("a =",a)
print("b =",b)
print('c =',c)