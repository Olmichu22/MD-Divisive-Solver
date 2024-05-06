import numpy as np

def diversity_matrix(samples, groups):
  """ Calcula la matriz de diversidad de una población de elementos samples, donde
  cada elemento pertenece a un grupo determinado y la diversidad entre dos elementos será
  0 si pertenecen al mismo grupo y 1 si pertenecen a grupos diferentes."""
  n_samples = samples.shape[0]
  div_matrix = np.zeros((n_samples, n_samples))
  for i in range(n_samples):
      for j in range(n_samples):
          div_matrix[i, j] = 0 if groups[i] == groups[j] else 1
  return div_matrix

def ordenar_indices(DA, X, in_bool, ascending):
  """ Ordena los índices de un array basado en los valores de otro array.
  Parámetros:
  - DA: array de valores a ordenar
  - X: array de valores binarios que indican si un índice debe ser considerado
  - in_bool: booleano que indica si se deben seleccionar los índices donde X es 1 (True) o 0 (False)
  - ascending: booleano que indica si el orden es ascendente (True) o descendente (False)
  Retorna:
  - Array de índices ordenados
  """
  # Filtramos los índices basados en el valor de 'in'
  if in_bool:
      # 'in' es True, seleccionamos índices donde X es 1
      indices_filtrados = np.where(X == 1)[0]
  else:
      # 'in' es False, seleccionamos índices donde X es 0
      indices_filtrados = np.where(X == 0)[0]
  
  # Ordenamos los índices filtrados basados en los valores en DA
  # El parámetro 'ascending' determina si el orden es ascendente o descendente
  # np.argsort() retorna los índices que ordenarían un array
  indices_ordenados = indices_filtrados[np.argsort(DA[indices_filtrados])]
  
  if not ascending:
      # Si 'ascending' es False, invertimos el orden
      indices_ordenados = indices_ordenados[::-1]
  
  return np.array(indices_ordenados)

def swap(X, j_index, k_index):
  """ Genera una nueva solución intercambiando dos elementos de X.
  j_index: índice del primer elemento a intercambiar (fuera de la solución)
  k_index: índice del segundo elemento a intercambiar (dentro de la solución)"""
  X_new = X.copy()
  X_new[j_index] = X[k_index]
  X_new[k_index] = X[j_index]
  return X_new
