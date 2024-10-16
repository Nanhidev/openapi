# Logical Operator 

a = 40
b = 30

print(a>b and a<b)
print(a<b and a<b)
print(a>b and a>b)

print()


print(a>b or a<b)
print(a<b or a<b)
print(a>b or a>b)

print()


print(not(a>b))
print(not(a<b))
print()


# membership Operator
print("MEMBERSHIP OPERATOR !") 
a = [10,20,30,40 , 50,60,70,80,90]
print(20 in a)
print(200 in a)

print(200 not in a)
print(20 not in a)
print()


# identify Operator
print("Identify OPERATOr !")

a = 2
b = 2
print(a is b)
print(a is not b)
print(id(a),id(b))
print(id(a)==id(b))
print()

a = 50 
b = 30
print(a is b)
print(a is not b)
print(id(a),id(b))
print(id(a)==id(b))