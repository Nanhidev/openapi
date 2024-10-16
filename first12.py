l = [12,45,65,78,65,34,67,78,90]
for i in l :
    print(i, end=" , ")

print()
print()

for i in [10,'nanhi',True, 10.20,5j,'deo']:
    print(i,type(i))
print()

for i in range(10):
    print(i,end=' . ')

print()


for i in range(21):
    if i%2 == 0 :
        print(i)
print()


n = int(input("Enter the any no :"))
sum = 0 
for i in range(n+1):
    sum = sum+i
print("Sum of first no",n ,'Numbers :',sum)


# n = 10
sum = 0
for i in range(10):
    if i%3 == 0 or i%5 == 0:
        sum = sum+i
print(sum)