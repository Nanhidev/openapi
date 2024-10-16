class great:
    def grest1(self):
        self.id = int(input('Enter the id :'))
        self.name = input('Enter the name :')
        self.address = input('Enter the address :')
        self.age = input('Enter the age :')

    def display(self):
        print('display id :',self.id)
        print('display name :', self.name)
        print('display address :',self.address)
        print('display age :',self.age)

s1 = great()
s1.grest1()
print()
s1.display()
