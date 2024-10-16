n = int(input("Enter the any no :"))
if n>= 1 and n<=100 :
    print("The number",n ,"is in between 1 to 100")

else :
    print('The number', n,'is not betbeen 1 to 100')

print()

n = int(input("Enter the no :"))
m = int(input("Enter the no :"))

if n>m :
    print(n,"N is big M :", m)
else :
    if n<m:
        print(n,"N is less M :",m)
    
    else:
        print(n,"N is equal to M :",m)