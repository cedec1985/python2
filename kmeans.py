import numpy as np   
from sklearn.utils import shuffle
# génération 100 points 3D suivant loi normale centrée
# chaque groupe est translaté d'un vecteur [3,3,3]
d1 = np.random.randn(100,3) + [3,3,3]
d2 = np.random.randn(100,3) + [-3,-3,-3]
d3 = np.random.randn(100,3) + [-3,3,3]
d4 = np.random.randn(100,3) + [-3,-3,3]
d5 = np.random.randn(100,3) + [3,3,-3]
# génération des étiquettes de chaque groupe
c1 = np.ones(100)
c2 = 2 * np.ones(100)
c3 = 3 * np.ones(100)
c4 = 4 * np.ones(100)
c5 = 5 * np.ones(100)
# concaténation des données dans une matrice
data = np.concatenate((d1,d2,d3,d4,d5))
labels = np.concatenate((c1, c2, c3, c4, c5))
print(data.shape)
# permutation aléatoire des lignes de la matrice data
data, labels = shuffle(data, labels)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# La couleur des points dépend de leur étiquette (label)
ax.scatter(data[:,0], data[:,1], data[:,2], c=labels)
plt.show()
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5, n_init=1, init='k-means++').fit(data)
pred = kmeans.predict(data)
print(kmeans.labels_)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:,0], data[:,1], data[:,2], c=pred)
plt.show()
from sklearn import metrics #Il est possible d’évaluer la cohérence entre les groupes de départ et le partitionnement trouvé par K-means en utilisant l’indice de Rand ajusté
metrics.adjusted_rand_score(pred, labels)
#Appliquez maintenant la classification automatique avec K-means avec un seul essai (n_init = 1) utilisant la méthode d’initialisation random
kmeans = KMeans(n_clusters=5, n_init=1, init='random').fit(data)
metrics.adjusted_rand_score(kmeans.labels_, labels)

#avec les textures
textures = np.loadtxt('texture.dat')
textures.reshape(1,-1)
np.random.shuffle(textures)
kmeans = KMeans(n_clusters=11).fit(textures[:,:40])
metrics.adjusted_rand_score(kmeans.labels_, textures[:,40])
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
try:
    lda = LinearDiscriminantAnalysis()
    lda.fit(kmeans.labels_,textures)
    rndt = lda.transform(kmeans)
    print(rndt.shape)
    plt.plot(rndt, lda, 'r+')
    plt.xlabel("Axe discriminant")
    plt.ylabel("Classe")
    plt.yticks([1, 2])
except: ValueError
finally:
    plt.show()

