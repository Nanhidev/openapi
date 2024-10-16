a = int(input("Enter the num1 :"))
b = int(input("Enter the Num2 :"))

if b == 0:
    print("Second no  cant be zero")

else :
    print("result is :",a/b)
print()


try :
    a = int(input("Enter the no :"))
    b = int(input("Enter the no2 :"))
    print("result is :", a/b)

except :
    print("Something went wrong")

print()

try :
    n = int(input("Enter thr no1 :"))
    m = int(input("Enter thr no2 :"))
    print('result is :',n/m)

except ZeroDivisionError as msg :
    print(msg)

except ValueError as msg:
    print(msg)