class Test :
    def m1(self):
        print('no arg method !')

    def m1(self,a):
        self.name = a
        print("one arg method !")

    def m1(self,a,b):
        self.name = a
        self.address = b
        print("two arg method !")
        

t = Test()
t.m1(30,40)
print()

class Test :
    def __init__(self) :
        print('no are constructor !')

    def __init__(self,a):
        print('one are constructor !')

    def __init__(self,a,b):
        print('two are constructor !')
    
T = Test(10,20)







