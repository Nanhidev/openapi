class A:
    def __init__(self,x,y,z):
        self.name = x
        self.address = y
        self.age = z


a = A('Anuja', 'Hyderabad', 23)
print(a.__dict__)

b = A('nanhi','Ameerpet',23)
print(b.__dict__)
