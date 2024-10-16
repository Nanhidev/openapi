class parent :
    x = 10
    _y = 200
    __z = 4000

class child(parent):
    print(parent.x)
    print(parent._y)
    # print(parent.__z)

t = child()
print(t.x)
print(t._y)
print()