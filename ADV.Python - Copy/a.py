class Student :
    '''Welcome to durgasoft !'''

a = Student()
print(a.__doc__)
print()

class Stud:
    def __init__(self):
        self.id = 1
        self.name = 'Rahul'
        self.surname = 'shrma'
        self.age = 23
        self.mail = 'rahuldeo@gmail.com'
        self.address = 'Bagloro'

    def S_details(self):
        print('S_Details id :',self.id)
        print('S_details name :',self.name)
        print('S_details surname :',self.surname)
        print('S_details age :',self.age)
        print('S_details mail :',self.mail)
        print('S_details address :',self.address)

b = Stud()
b.S_details()
print()

b1 = Stud()
b1.S_details()