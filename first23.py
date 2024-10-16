list = [12,34,56,78,90,13,24,46,68]
print(list)
list.remove(90)  # This is remove method !
print()

list.pop()          # this is deleted end value
print(list)
print()

list.pop(4)      # it's deleted 4 number value !
print(list)
print()

list.clear()  # it's doing empty list !
print(list)
print()

# del list
# print(list)

list1 = ["Diksha","Vaibhvi","Ishika","Priya","Nanhi"]
list2 = [10,20,30,40]
print(list1+list2)
print(list1*4)
print(list2*2)
print()

# list sort

list = [90,45,56,23,90,45,344,34,23,56,34,123,45,34]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print()

list4 = [90,45,56,23,90,45,344,34,23,56,34,123,45,34]
list4.sort()
print(list4)

list = list4.sort(reverse=True)
print(list)

