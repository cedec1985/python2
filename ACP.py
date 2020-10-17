import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

rndn3d = np.random.randn(500,3)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(rndn3d[:,0], rndn3d[:,1], rndn3d[:,2])
plt.title("Données initiales")
plt.show()
from sklearn.decomposition import PCA  #ACP

pca = PCA(n_components=3)
pca.fit(rndn3d)

print("Pourcentage de variance expliquée : ")
print(pca.explained_variance_ratio_)
print("Composantes principales : ")
print(pca.components_)
s1 = np.array([[3,0,0],[0,1,0],[0,0,0.2]])  # matrice de déformation
r1 = np.array([[0.36,0.48,-0.8],[-0.8,0.6,0],[0.48,0.64,0.6]])  # matrice de rotation
rndef = rndn3d.dot(s1).dot(r1)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(rndef[:,0], rndef[:,1], rndef[:,2])
plt.title("Données déformées")
plt.show()
pca = PCA(n_components=3)
pca.fit(rndef)

print("Pourcentage de variance expliquée : ")
print(pca.explained_variance_ratio_)
print("Composantes principales : ")
print(pca.components_)

mammals = np.loadtxt('mammals.csv', delimiter=';', usecols=[1,2,3,4,5,6,7,8,9,10], skiprows=1)
print(mammals[:2,:])
noms = np.genfromtxt('mammals.csv', dtype='str', delimiter=';', usecols=[0], skip_header=1)
print(noms)

mammalsCR= np.array([[ 1., 0.,1.],[-1.,1.,0.],[2.,1.,0.]])
pcaCR = preprocessing.scale(mammalsCR)
print(pcaCR)

print(pcaCR.mean)

print(pcaCR.std)
pcaCR = preprocessing.StandardScaler().fit(pcaCR)

mNt = pcaCR.transform(mammalsCR) 
print(mNt[:2,:])
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111,projection='3d')
for i in range(len(noms)):
    try:
        x=mNt[i,0]
        y=mNt[i,1]
        z=mNt[i,2]
        ax.scatter(x,y,z)
        ax.text(x,y,z,noms[i])
    except: TypeError
    finally:
        plt.show()

s1 = np.array([[3,0,0],[0,1,0],[0,0,0.01]])  # matrice de déformation
r1 = np.array([[0.36,0.48,-0.8],[-0.8,0.6,0],[0.48,0.64,0.6]])  # matrice de rotation

# On génère deux nuages de points déformés et tournés
rndn3d1 = np.random.randn(500,3)
rndef1 = rndn3d1.dot(s1).dot(r1)
rndn3d2 = np.random.randn(500,3)
# Le deuxième nuage de point est translaté selon l'axe z
rndef2 = rndn3d2.dot(s1).dot(r1) + [0, 0, 1]
rndef= np.concatenate((rndef1, rndef2))
print(rndef.shape)
lcls1 = np.ones(500)
lcls2 = 2 * np.ones(500)
lcls = np.concatenate((lcls1, lcls2))
print(lcls)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(rndef[:,0], rndef[:,1], rndef[:,2], c=lcls)
plt.show()
lda = LinearDiscriminantAnalysis()
lda.fit(rndef,lcls)

rndt = lda.transform(rndef)
print(rndt.shape)

plt.plot(rndt, lcls, 'r+')
plt.xlabel("Axe discriminant")
plt.ylabel("Classe")
plt.yticks([1, 2])
plt.show()

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(rndef)

rndp = pca.transform(rndef)
print(rndp.shape)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(rndp[:,0], rndp[:,1], c=lcls)
plt.show()

lda = LinearDiscriminantAnalysis()
lda.fit(rndp,lcls)
rndpt = lda.transform(rndp)

plt.plot(rndpt, lcls, 'r+')
plt.xlabel("Axe discriminant")
plt.ylabel("Classe")
plt.yticks([1, 2])
plt.show()