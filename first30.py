d = {}
print(type(d))
print(d)
print()

d1 = {'id':20 , "name" : "Nanhi" , "surname": "Deo", 'distic': "Saharsa",'password':"12345deo"}
print(d1)
print(d1['distic'])
print(d1.get('password'))
print()

print(d1.get('age'))
d1['age'] = 20
print(d1)
print()

d1['name']='Sunil deo'
print(d1)
print()

d1['age']= 55
print(d1)
print(d1)
print()

d = d1
print(d)
d3 = d1.copy()
print(d3)
print(id(d1))
print(id(d3))
print()

print(d1.items())
print(d1.keys())
print(d1.values())
print()

d1.update({'State':"Bihar","village":"Bihra"})
print(d1)
print()

dic = {'id':20 , "name" : "Nanhi" , "surname": "Deo", 'distic': "Saharsa",'password':"12345deo"}
print(len(dic))
print('surname' in dic)
print('surname' not in dic)
print('Deo' in dic)
print('Deo' not in dic)
print()

print('State' in dic)
print('State' not in dic)