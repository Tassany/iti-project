import numpy as np
from collections import Counter

# metric function
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum(x1-x2)**2)

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        # compute distances
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # get k nearest samples, and their labels
        k_indexes = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indexes]
        # majority vote, get most common class label
        # Counter().most common returns a list of tuples
        # where the first element of the tuple is the label, and the second is its frequence: [(label, frequence)]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]