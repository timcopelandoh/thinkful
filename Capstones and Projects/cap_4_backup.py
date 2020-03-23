from sklearn import metrics 
from scipy.spatial.distance import cdist

X = content_vector.iloc[:,1:]

distortions = []
inertias = []
sil = []

k_range = range(2,200)

for k in k_range:
    model = MiniBatchKMeans(n_clusters = k).fit(X)
    distortions.append(sum(np.min(cdist(X, model.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
    inertias.append(model.inertia_)
    sil.append(metrics.silhouette_score(X, model.predict(X), metric='euclidean'))
    

plt.figure(figsize=(12,6))    
    
plt.subplot(1,3,1)
plt.title('Distortion by Cluster Size')
plt.plot([x for x in k_range], distortions)

plt.subplot(1,3,2)
plt.title('Intertia by Cluster Size')
plt.plot([x for x in k_range], inertias)

plt.subplot(1,3,3)
plt.title('Silhouette Score by Cluster Size')
plt.plot([x for x in k_range], sil)

plt.show()

----------------------------------------------------------------------------------------------------------


plt.figure(figsize=(12,6))    
    
plt.subplot(1,3,1)
plt.title('Distortion by Cluster Size')
plt.plot([x for x in k_range], distortions)

plt.subplot(1,3,2)
plt.title('Intertia by Cluster Size')
plt.plot([x for x in k_range], inertias)

plt.subplot(1,3,3)
plt.title('Silhouette Score by Cluster Size')
plt.plot([x for x in k_range], sil)

plt.show()


----------------------------------------------------------------------------------------------------------

distortions = []
inertias = []
sil = []

k_range = range(2,200)

for k in k_range:
    model = MiniBatchKMeans(n_clusters = k).fit(user_likes_vector.iloc[:,1:])
    distortions.append(sum(np.min(cdist(user_likes_vector.iloc[:,1:], model.cluster_centers_, 'euclidean'), axis=1)) / user_likes_vector.shape[0])
    inertias.append(model.inertia_)
    sil.append(metrics.silhouette_score(user_likes_vector.iloc[:,1:], model.predict(user_likes_vector.iloc[:,1:]), metric='euclidean'))

plt.figure(figsize=(12,6))    
    
plt.subplot(1,3,1)
plt.plot([x for x in k_range], distortions)

plt.subplot(1,3,2)
plt.plot([x for x in k_range], inertias)

plt.subplot(1,3,3)
plt.plot([x for x in k_range], sil)

plt.show()


----------------------------------------------------------------------------------------------------------




----------------------------------------------------------------------------------------------------------




----------------------------------------------------------------------------------------------------------




----------------------------------------------------------------------------------------------------------

