s = "Python is very easy to understanding language and it is oop and it is interpreter !"

substring = ("is")
print(s.count(substring))
print(s.count('language'))
print(s.count('s'))
print(s.count(" "))
print()

s2 = "my name is Nanhi Deo"
print(s2)

s3 = s2.replace("Nanhi" , "Sunil")
print(s3)
print(s2.replace('Nanhi','Bhashkar'))
print()

print("".join("My mother name is Babita devi !"))
print(" , ".join(['sai','durga','ishika','anuja','diksha']))
print()

print(" ".join(reversed(["sai","nanhi deo","Priya di","Anuja","Bharti"])))
s = ('Abhilasha Shinha','Alok Ranjan', 'Aush Ranjan','Akshay Ranjan','Bhashkar Deo','Nanhi Deo')
print(s[::-1])
print()

l = (" , ".join("india is best country !"))
print(l[::-1])

print("".join(reversed('indian is great country !')))