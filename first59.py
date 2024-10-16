
# import numpy as np

# A = np.array([[10,20,30],[34,56,78],[78,35,23]])
# print(A.dtype)
# print(A)
# print()

# print(A.ndim)
# print(A.shape)
# print(A.size)
# print(A[1][2])
# print()


import numpy as np 

A = np.array([[10,20,30,-40],[34,56,-67,34],[80,-45,34,56]])
print(A)
print()
print('Max element is :',A.max())
print("Min element is :",A.min())
print()

print('col wise max element is :',A.max(axis=0))
print('col min element is :',A.min(axis=0))
print()

print("row element max is :",A.max(axis=1))
print('row element min is :',A.min(axis=1))
print(A.sum())
print()


