d = {'id':20 , "name" : "Nanhi" , "surname": "Deo", 'distic': "Saharsa",'password':"12345deo"}
print(d)
print(d.pop('name'))
print(d.popitem())
print(d)
print()


x = [10,30,50,70,80,255]
print(x)

b = bytes(x)
print(b)
b = bytearray(x)
print(b)

print(b[0])
print(b[-1])

b[3]=45
print(b)

for i in b:
    print(i)