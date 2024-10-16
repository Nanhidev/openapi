class Branch :
    def getbranchdata(self):
        self.bcode = int(input('Enter branch cord :'))
        self.bname = input('enter the branch name :')
        self.baddress = input('enter the branch address :')

    def displaybranchdata(self):
        print("Branch code is :", self.bcode)
        print("Branch name is :", self.bname)
        print("Branch address is :", self.baddress)




class Employee(Branch):
    def getempdata(self):
        self.eid = int(input('Enter the id :'))
        self.ename = input('Enter the name :')
        self.eaddress = input('enter the address :')

    def displayempdata(self):
        print('Employee id is :',self.eid)
        print('Employee name is :', self.ename)
        print("Employee address is :",self.eaddress)

class Salary(Employee):
    def getsal(self):
        self.basic = int(input('Enter the basic salary :'))

    def calculeate(self):
        self.DA = self.basic*0.06
        self.HRA = self.basic*0.4
        self.Gross = self.basic+self.DA+self.HRA

    def display(self):
        print('Basic is :',self.basic)
        print('DA is :',self.DA)
        print('HRA is :',self.HRA)
        print('Gross is :',self.Gross)


S = Salary()
S.getbranchdata()
S.displaybranchdata()
print()

S.getempdata()
S.displayempdata()
print()

S.getsal()
S.calculeate()
S.display()