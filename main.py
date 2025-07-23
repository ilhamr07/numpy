import numpy as np

#membuat vector
a= np.array([1,2,3,4,5])
b= [1,2,3,4,5]

#membuat vector dengan range
c= np.arange(1,10,2)

#membuat linspace (membagi data menjadi 4 bagian)
d = np.linspace(1,10,4)

#membuat matrix
e = np.array( [(1,2,3) , (4,5,6)])

#membuat matrix denan nilai 0
f= np.zeros((5,5))

#membuat matrix dengan nilai 1
g=np.ones((5,5))

#matrix identitas
h = np.identity(5)

#display
print(h)

