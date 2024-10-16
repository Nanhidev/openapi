import datetime
X = datetime.datetime.now()
print(X)
print()

from datetime import *
X = datetime.now()
print(X)
print(X.date())
print(X.time())
print()

print(X.strftime('%A'))      #Week day full version      !
print(X.strftime("%a"))                # Week day short version !
print()

print(X.strftime('%B'))     # Month full version !
print(X.strftime("%b"))          # month short version !
print()

print(X.strftime("%Y"))           # Year full version !
print(X.strftime("%y"))              # year short version !
print()

from calendar import *

X = 1947
m = 8
print(month(X,m))
print(month(2024,8))
print()

from calendar import *
print(calendar(2024, 3 , 1 , 9 ))