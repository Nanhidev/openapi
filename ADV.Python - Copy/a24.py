from abc import ABC , abstractmethod

class Vihicle(ABC):
    @abstractmethod
    def Wheels(self):
        pass

    def engine(self):
        print("Bs6 engine !")

    
    @abstractmethod
    def color(self):
        pass


class Car(Vihicle):
    def Wheels():
        print('Car : 4 Wheels')

    def color(self):
        print("Car : color is red !")

class Bike(Vihicle):
    def Wheels(self):
        print("Bike : 2 Wheels")

    def color(self):
        print("Bike : Color is Black")



c= Car()
c.Wheels()
# c.engine()
c.color()


b = Bike()
b.Wheels()
# b.engine()
b.color()