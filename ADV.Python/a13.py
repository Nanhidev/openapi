class Test :
    x = 60                    # public
    _x = 600                           # protected
    __x = 60000                                  # private


    def __init__(self): 
        print("Withing the class !")
        print(self.x)
        print(self._x)
        print(self.__x)

t = Test()

print("Outside of the class")
print(t.x)
print(t._x)
# print(t.__x)  private class


