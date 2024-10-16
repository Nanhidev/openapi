s = [45,34,56,78,34,22,55,44,123,90,80]
print(s)

for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if(s[i]>s[j]):
            s[i],s[j] = s[j],s[i]

print(s)
print()


list = [10,20,30,30,40,50,50,60,70,20]
lis = []
list2 = []

for i in list:
    if i not in lis:
        lis.append(i)

    else :
        list2.append(i)
print(list2)

print()


sum = 0
for i in range(1000):
    if i%3==0  or i%5==0 :
        sum = sum+i
print(sum)