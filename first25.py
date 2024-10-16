l = [324,465,34,'AnuRadha',None,"Radhika",'Bhagymani',34,43,34,34]
print(l.count("Radhika"))
print(l.count(34))
print(l.count("nanhi"))
print(l.count(100))
print()


lis = []
item = int(input("Enter the int value :"))
item1 = input("enter the str value :")
item2 = float(input("Enter the Float no :"))

# lis.extend([item ,item1 , item2])
# print(lis)
# print()

lis.append(item)
lis.append(item1)
lis.append(item2)
print(lis)
print()


a = []
n = int(input("Enter the length of the list :"))
for i in range (n):
      m = int(input("Enter the value :"))
      a.append(m)
      print(a)