import numpy as np
from scipy.spatial import distance

def D(x):
  """ Calcula la matriz de distancias euclídeas entre los elementos de x."""
  return distance.squareform(distance.pdist(x))
  
def MD(X, D_matrix):
  """ Calcula la diversidad de la solución X, según la matriz de diversidad D_matrix."""
  return np.dot(np.dot(X,D_matrix), X.T)/2

def DA(X,D_matrix):
  """ Calcula la diversidad aportada por cada elemento de X, según la matriz de diversidad D_matrix."""
  return np.dot(D_matrix, X.T)

def min_DA(X, DA_matrix, seed = 0):
  """ Devuelve el índice del elemento de X que minimiza la diversidad aportada
  por el resto de elementos de X, según la matriz de diversidad DA_matrix."""
  M_els = DA_matrix[X == 1]
  min_da = np.min(M_els)
  min_index = np.where(DA_matrix == min_da)[0]
  # De min index, seleccionamos aquel que esté en X
  # Como puede haber varios, seleccionamos uno aleatorio, determinado por seed
  np.random.seed(seed)
  ind = np.random.randint(0, len(min_index[X[min_index] == 1]))
  tot_index = len(min_index[X[min_index] == 1])
  # Seleccionamos uno de los indices que estén en M y lo devolvemos
  min_index = min_index[X[min_index] == 1][ind]
  return min_index, (ind, tot_index)