import numpy as np
from numpy import newaxis
from scipy import linalg
import matplotlib.pyplot as plt
geyser=np.loadtxt('geyser.txt',delimiter=' ') #ouvrir un fichier texte
print(geyser.shape)
print(geyser[:10,:])
np.savetxt('geyserv_nouveau.txt', geyser, delimiter=', ') #créer un fichier texte
tu2d = np.ones((2,2))
tb2d = np.ones((2,2)) * 2
tcl = np.concatenate((tu2d,tb2d))
print(tcl) #concaténer
tcl = np.vstack((tu2d, tb2d))
tcl = np.hstack((tu2d, tb2d))
tu1d = np.ones(2)
#modifier ou ajouter des axes à un tableau
print(tu1d)

print(tu1d[:,newaxis])

print(np.column_stack((tu1d[:,newaxis],tb2d)))

print(np.hstack((tu1d[:,newaxis],tb2d)))
print(tcl > 1)

print(tb2d * tb2d)

tb2d += tu2d
print(tb2d)
g0 = geyser[:2,:]
print(g0)

g0.transpose()
#vectoriser
def addsubtract(a,b):
    if a > b:
        return a - b
    else:
        return a + b

print(addsubtract(2,3))

vec_addsubtract = np.vectorize(addsubtract)
print(tu2d)

print(g0)

print(vec_addsubtract(g0,tu2d))

print(linalg.det(g0))

print(linalg.norm(g0))  

print(linalg.norm(g0,'fro'))

print(linalg.norm(g0,1))

print(linalg.eig(g0))

mammals248 = np.loadtxt('mammals.csv', delimiter=';', usecols=[2,4,8], skiprows=1)
print(mammals248[:5,:])

noms = np.genfromtxt('mammals.csv', dtype='str', delimiter=';', usecols=[0], skip_header=1)
print(noms)
#avec matplotlib
from mpl_toolkits.mplot3d import Axes3D  
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(noms)):
        x,y,z = mammals248[i,0],mammals248[i,1],mammals248[i,2]
        ax.scatter(x,y,z)
        ax.text(x,y,z,noms[i])
plt.show()