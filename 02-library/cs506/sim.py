import numpy as np
from scipy.spatial.distance import pdist
from sklearn.metrics.pairwise import cosine_similarity

def euclidean_dist(x, y):
    x = np.array(x)
    y = np.array(y)
    p = np.sum((x-y)**2)
    d = np.sqrt(p)
    return d
    # raise NotImplementedError()


def manhattan_dist(x, y):
    x = np.array(x)
    y = np.array(y)
    return sum(abs(x-y))
    # raise NotImplementedError()

def intersection(x,y):
    return list(set(x)&set(y))
def union(x,y):
    return list(set(x)|set(y))
    
def jaccard_dist(x, y):
    if x ==[] and y == []:
        return "lengths must not be zero"
    d = 1 - len(intersection(x,y))/len(union(x,y))
    return d



def cosine_sim(x, y):
    if x == [] and y == []:
        return "lengths must not be zero"
    if len(x) != len(y):
        return "lengths must be equal"
    x = np.array(x)  
    y = np.array(y)   
    op7=np.dot(x,y)/(np.linalg.norm(x)*(np.linalg.norm(y)))  
    return op7
    # raise NotImplementedError()
# Feel free to add more
