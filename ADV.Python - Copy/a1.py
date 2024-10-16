class emp:
    def __init__(self,id,name,address,age):
        self.id = id
        self.name = name
        self.address = address
        self.age = age

    def details(self):
        print('Emp_Details id :',self.id)
        print('Emp_Details name :',self.name)
        print('Emp_Details address :',self.address)
        print('Emp_Details age :',self.age)

s = emp(1, 'Nanhi', 'Hyd', 20)
s.details()
print()


s1 = emp(2,'Ishika','Hyd', 24)
s1.details()
