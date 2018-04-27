#I Putu Indra Aristya - 1301154219

from numpy import genfromtxt, math
import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
fig = plot.figure()
ax = fig.add_subplot(111, projection='3d')


dataTrain = genfromtxt('Workbook2.csv',delimiter=',') #workbook2.csv adalah file data latih

att1 = dataTrain[:,0]
att2 = dataTrain[:,1]
att3 = dataTrain[:,2]
kelas = dataTrain[:,3]

#------Code untuk visualisasi data latih dengan scatter plot------
ax.scatter(xs=att1, ys=att2, zs=att3,c=kelas)
plot.show()


#------Code Fungsi-----
smooth = 0.9
T = 0

def pangkat(x,y,z,xtrain,ytrain,ztrain):
    pangkatexp = -1*((((x-xtrain)**2) + ((y-ytrain)**2) + ((z-ztrain)**2)) / ((smooth)**2))
    return pangkatexp

def exponen(x):
    return math.exp(x)

def classification0(y):
    x = 1/(32*smooth) #32 adalah jumlah data latih dengan kelas 0
    return x*y

def classification1(y):
    x = 1 / (31 * smooth) #31 adalah jumlah data latih dengan kelas 1
    return x * y

def classification2(y):
    x = 1 / (37 * smooth) #37 adalah jumlah data latih dengan kelas 2
    return x * y

#-----Code Proses-----

label0 = 0
label1 = 0
label2 = 0

o = 0
hasil = [0]*50


#melakukan penghitungan dengan PDF pada fungsi pangkat dan eksponen
for i in range(100,150):
    for j in range(0,100):
        x = pangkat(dataTrain[j,0],dataTrain[j,1],dataTrain[j,2],dataTrain[i,0],dataTrain[i,1],dataTrain[i,2])
        y = exponen(x)

        #hasil perhitungan data dengan PDF yang kelasnya sama, dijumlahkan (sum function)
        if (dataTrain[j,3] == 0.0):
            label0 = label0 + y
        elif (dataTrain[j,3] == 1.0):
            label1 = label1 + y
        elif (dataTrain[j,3] == 2.0):
            label2 = label2 + y

    #dilakukan penghitungan klasifikasi dengan rumus (1/n*sigma)*(jumlah perhitungan PDF) dimana n adalah jumlah data dengan kelas data tersebut
    label0 = classification0(label0)
    label1 = classification1(label1)
    label2 = classification2(label2)


    #akan ditentukan nilai kelas paling besar yang menjadi hasil prediksi kelas dari data tersebut
    if (label0 > label1 and label0 > label2):
        hasil[o] = 0
        o = o + 1
    elif (label1 > label0 and label1 > label2):
        hasil[o] = 1
        o = o + 1
    elif (label2 > label0 and label2 > label1):
        hasil[o] = 2
        o = o + 1

    label0 = 0
    label1 = 0
    label2 = 0
    print(hasil[o-1])

#melakukan perhitungan akurasi
j = 100
for i in range(0,50):
    if (int(hasil[i]) == (int(dataTrain[j,3]))):
        T = T+1
    j = j+1

print((T/50)*100)