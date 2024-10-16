# class Book:
#     def __init__(self,pages) :
#         self.Pages = pages

#     def __add__(self,other):
#         return self.pages+other.pages
    
#     def __mult__(self,other):
#         return self.pages+other.pages

# b1 = Book(10)
# b2 = Book(20)
# print(b1+b2)
# print(b1*b2)


class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def __mul__(self,other):
        return self.salary*other.days 
    
class TimeSheet :
    def __init__(self,name,days):
        self.name = name
        self.days = days

e = Employee('Durga',5000)
t = TimeSheet('Soft', 20)
print('This Month is Salary :',e*t)


