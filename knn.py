from scipy import spatial
class knn():
  K = 0
  X_train = ''
  y_train = ''
  def __init__(self,k):
    self.K = k
  def fit(self,features,labels):
    self.X_train = features
    self.y_train = labels
  def euclidean_distance(self,x,y):
    return spatial.distance.euclidean(x, y)
  def sort_distance(self,x):
    return dict(sorted(x.items(), key=lambda y:y[1]))
  def common(self,lst):
    return max(set(lst), key=lst.count)
  def predict(self,feature):
    dist = {}
    first_k_values = []
    for i in range(len(feature)):
      for j in range(len(X_train)):
        distance = euclidean_distance(X_train.iloc[j],feature.iloc[i])
        dist[j] = distance
    distance_sorted = self.sort_distance(dist)
    first_k_value  = list(distance_sorted.items())[:self.K]
    for i,j in first_k_value:
      first_k_values.append(self.y_train.iloc[i])
    return self.common(first_k_values)
