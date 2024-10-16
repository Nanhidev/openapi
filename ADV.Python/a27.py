import os
try :
    print('try block')

except :
    print('Except block')
    os._exit(0)

finally:
    print('Finally Block')

print()


try :
    print("outer try")
    try :
        print(10/0)
        print("Inner try")

    except ValueError:
        print("Inner Except !")
    
    finally :
        print("Inner Finally !")

except :
    print("outer except !")

finally:
    print("Outer finally")