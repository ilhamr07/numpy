import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

#stacking matrix | menumpuk matrix kebelakang
#horizontal stack
c = np.hstack((b,a))
print(c)

#vertikal stack
d= np.vstack((a,b))
print(d)



#test menggunakan matrix
print("ini bagian matrix")

aMat=np.zeros((3,4)) # cara baca (baris , kolom)
bMat=np.ones((3,4)) #(baris , kolom)

print(aMat)
print()
print(bMat)

print("ini bagian stacking matrix")
cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat))

print(cMat)
print(dMat)
