#I Putu Indra Aristya - 1301154219


from numpy import genfromtxt, math
import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
fig = plot.figure()
ax = fig.add_subplot(111, projection='3d')


dataTrain = genfromtxt('Workbook2.csv',delimiter=',')
dataTest = genfromtxt('datatestPNN.csv',delimiter=',')

att1 = dataTrain[:,0]
att2 = dataTrain[:,1]
att3 = dataTrain[:,2]
kelas = dataTrain[:,3]

#------Code untuk visualisasi data dengan scatter plot------
#ax.scatter(xs=att1, ys=att2, zs=att3,c=kelas)
#plot.show()


#------Code Fungsi-----


T = 0

def pangkat(x,y,z,xtrain,ytrain,ztrain):
    pangkatexp = -1*((((x-xtrain)**2) + ((y-ytrain)**2) + ((z-ztrain)**2)) / ((smooth)**2))
    return pangkatexp

def exponen(x):
    return math.exp(x)

def classification0(y):
    # duaphi = (((math.pi*2)**(3/2)) * (smooth**3) * 32)
    # x = 1/(32*math.sqrt(duaakar))
    # x = 1/duaphi
    x = 1/(32*smooth)
    return x*y

def classification1(y):
    # duaakar = math.pi*2
    # x = 1/(31*math.sqrt(duaakar))
    # return x*y
    # duaphi = (((math.pi * 2) ** (3 / 2)) * (smooth ** 3) * 31)
    # x = 1/(32*math.sqrt(duaakar))
    # x = 1 / duaphi
    x = 1/(31 * smooth)
    return x * y

def classification2(y):
    # duaakar = math.pi*2
    # x = 1/(37*math.sqrt(duaakar))
    # return x*y
    # duaphi = (((math.pi * 2) ** (3 / 2)) * (smooth ** 3) * 37)
    # x = 1/(32*math.sqrt(duaakar))
    # x = 1 / duaphi
    x = 1/(37 * smooth)
    return x * y

#-----Code Proses-----

label0 = 0
label1 = 0
label2 = 0

o = 0
hasil = [0]*50
p = 0.1
while (p<1): #mencari nilai smooth terbaik antara 0.1 - 0.9
    # print(p)
    smooth = p
    # smooth = np.copy(p)
    # for i in range(0,50):
    #     for j in range(0,150):
    for i in range(100,150):
        for j in range(0,100):
    #         x = pangkat(dataTrain[j,0],dataTrain[j,1],dataTrain[j,2],dataTrain[i,0],dataTrain[i,1],dataTrain[i,2])
            x = pangkat(dataTrain[j, 0], dataTrain[j, 1], dataTrain[j, 2], dataTrain[i, 0], dataTrain[i, 1], dataTrain[i, 2])
            y = exponen(x)
            if (dataTrain[j,3] == 0.0):
                label0 = label0 + y
            elif (dataTrain[j,3] == 1.0):
                label1 = label1 + y
            elif (dataTrain[j,3] == 2.0):
                label2 = label2 + y

        label0 = classification0(label0)
        label1 = classification1(label1)
        label2 = classification2(label2)

        if (label0 > label1 and label0 > label2):
            hasil[o] = 0
            # print(hasil[o])
            o = o + 1
        elif (label1 > label0 and label1 > label2):
            hasil[o] = 1
            # print(hasil[o])
            o = o + 1
        elif (label2 > label0 and label2 > label1):
            hasil[o] = 2
            # print(hasil[o])
            o = o + 1

        label0 = 0
        label1 = 0
        label2 = 0
        # print("-----")
        #print(hasil[o-1])

    j = 100
    for i in range(0,50):
        if (int(hasil[i]) == (int(dataTrain[j,3]))):
            T = T+1
        j = j+1

    print("P = ",p,"Akurasi = ",(T/50)*100)
    o = 0
    T = 0
    j = 0
    p += 0.1