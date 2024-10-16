class Car :
    def __init__(self):
        self.__updatesoftware()

    def __updatesoftware(self):
        print('Updating Software')

c = Car()
print()


class Car:
    _name = ""
    __maxspeed = 10
    print(__maxspeed)

    def __init__(self):
        self._name= 'Nanhi deo'
        self.__maxspeed = 100
        print(self._name)
        print(self.__maxspeed)

    def drive(self):
        self.__maxspeed = 200
        print('Driving')
        print(self._name)
        print(self.__maxspeed)



S = Car()
S.drive()