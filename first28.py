s = set()
print(s)
print(type(s))
print()


set = {123, "nanhi" , None , "deo",23.34}
print(set)
print(type(set))

set.add("Bhagymani")
print(set)
print()

set.update([34,45,"Anuja",'Bolebaba'])
print(set)
print()


set1 = {234, "Nanhi", None , "Diksha" , 'Ishika', 45.45 , 4000}
print(set1)
set1.discard(None)
print(set1)
print()

set1.remove(45.45)
print(set1)
print()

s1 = set1.discard(100) # Answer = None
print(s1)
print()


set1.clear()
print(set1)








