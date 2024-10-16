f = "durgasoftwarehyderabadmatrivanam !"
print(f)
print(f.startswith('a'))  # this is False
print(f.startswith('d'))   # this is True
print()

print(f.endswith('o'))  # this is False 
print(f.endswith('!'))    # This is True !

print()

s = "1234567"
print(s.isdigit())  # this is True !
s = '123456a'
print(s.isdigit())     # this is False !
print()

a = "Abcd"
print(a.isalnum())      # This is True !

a = 'asdd123'
print(a.isalpha())          # it's True !


