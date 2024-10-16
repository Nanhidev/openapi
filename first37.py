def add(x , y):
    return x + y 

def sub(x , y):
    return x-y

def mult(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Salect Operation !")
print("1.addition !")
print("2.subtration !")
print('3.multiplcation !')
print('4.divide !')

choice = input("Enter the choice (1/2/3/4) :")
num = int(input("Enter the First no :"))
num2 = int(input("Enter the second no :"))

if choice == '1' :
    print(num, "+", num2, "=",add(num,num2) )

elif choice == '2':
    print(num,'-',num2 ,'=',sub(num,num2))
elif choice == '3' :
    print(num,'*',num2 ,'=',mult(num,num2))
elif choice == '4' :
    print(num,'/',num2,'=',divide(num,num2))

else :
    print("invalid no !")
print()


n = int(input("Enter the first no :"))
m = int(input("Enter the second no :"))
choice = input("Enter the choice symbol(+/-/*//) :")
if choice == '+':
    print("addition is :",n+m)

if choice == '-':
    print('subtraction is :',n-m)
    
if choice =='*':
    print("multiply is :",n*m)

if choice == '/':
    print('divide is :',n/m)

if choice !="-" and choice !='+' and choice !="*" and choice !="/" :
    print("imvalid value !")