import numpy as np

def kuadrat(a,b): #(baris, kolom)
    return b**2 #membuat kuadrat dari setiap kolom
a = np.fromfunction(kuadrat,(1,4), dtype=int) #fromfunction(namafungsi, shape(baris,kolom), typedata)
print("ini matrix 1 baris : \n",a)



def jumlah(a,b): #(baris, kolom)
    return b+1 #jumlahkan 1 untuk setiap kolom

#membuat matrix menggunakan fromfunction
b = np.fromfunction(kuadrat,(3,5), dtype=int)
print("ini matrix banyak baris:\n",b)
