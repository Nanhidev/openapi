s = {23,56,78,90,80,"Anuja","Bhashkar", True,34}
s1 = {78,45,56,80,90,"Bhagymani",False,23}
print(s)
print()

print(s|s1)
print(s.union(s1))
print()

print(s&s1)
print(s.intersection(s1))
print()


print(s-s1)
print(s1.difference(s))
print()

print(s^s1)
print(s1.symmetric_difference(s))
print()

set = {30,40,50,60,70,80,90,45,56,78,34}
print(len(set))
print(min(set))
print(max(set))
print(sum(set))
print(sum(set,5))
print()
print()


set1 = {23,45,-90,-80,54,67,89,34,56}
print(set1)
print(50 in set1)
print(50 not in set1)
print(-90 in set1)
print(-90 not in set1)