import numpy as np

a = np.array(([1,2],
              [3,4]))
b = np.ones([2,2])
print("matrix a")
print(a)

print("matrix b")
print(b)

#perkalian matrix
c = np.dot(a,b)
print("matrix c")
print(c)