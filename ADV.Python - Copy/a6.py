class test :
    a = 1000        # static variable

    def __init__(self):
        self.b = 2000                 # intance variable

t = test()
print('t :',t.a, t.b )

t1 = test()
print('t1 :',t1.a, t1.b)

test.a = 500
t.b = 50000
print('t :',t.a, t.b)
print('t1 :', t.a , t.b)