list = [13,56,76,89,45,34,'nanhi',True,False,'diksha',35.57,65,345]
print(list)
print()


list2 = list.copy()      # this is shallow
list[2] = "DEO NANHI"
print(list2)      


print(list)
print()

list5 = list          # deep copy
print(list5)
print(id(list5))
print(id(list))
print(id(list2))

list5[6] = 'rtsgtg'
print(list)
print(list5)
print(list2)