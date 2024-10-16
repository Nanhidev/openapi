s = "Python is very easy to understanding language !"
print(s)
s1 = s.split(" ")
print(s1)
print(type(s1))
s1.sort()
print(s1)
s1.sort(reverse=True)
print(s1)
print()

s = "DURGA soft ware Hyderabad !"
print(s)
print(s.swapcase())
print()

s = "DURGA SOFT WARE !"
print(s)
print(s.strip(" "))
print()

d = "adurga"
print(d.split("a"))
print(d.strip("a"))
print(d.lstrip('a'))
print(d.rstrip("a"))
print()

print(len("My institute name is DurgaSoftWareSolutionMtrivanam !"))
