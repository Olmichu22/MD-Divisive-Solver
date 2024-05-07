import numpy as np
import time
from divisive_solver.reward_functions import MD, D, DA, min_DA
import matplotlib.pyplot as plt

def MD_problem_heuristic(N, M_dim, seed, verbose = False ,D_matrix=None, plot_int = 30):
  """ Resuelve el problema de maximización de diversidad de una población N
  de tamaño tot_dim, seleccionando M_dim elementos de la misma. La solución
  se obtiene mediante un algoritmo heurístico que selecciona en cada paso
  el elemento que minimiza la diversidad aportada por el resto de elementos
  de la solución.
  Parámetros:
  - N: Población de elementos a seleccionar
  - M_dim: Número de elementos a seleccionar
  - seed: Semilla para reproducibilidad
  - verbose: Si True, muestra información adicional
  - D_matrix: Matriz de diversidad de la población N. Si no se proporciona,
    se calcula a partir de la distancia euclídea entre los elementos de N.
  - plot_int: Cada cuántas iteraciones se muestra un plot de la solución
  
  Devuelve:
  - X: Vector binario con la solución
  - data: Diccionario con información adicional de la solución
  - diversity_matriz: Matriz de diversidad de la población N
  """
  # Reepresentación de solución
  X = np.ones(len(N))

  # Matriz de diversidad
  if D_matrix is not None:
    diversity_matriz = D_matrix
  else:
    diversity_matriz = D(N)
  
  MD_i = []
  election_i = []
  totel_i = []
  iter_i = 0
  time_i = time.time()
  sol_i = []
  while sum(X) > M_dim:
    DA_matrix = DA(X, diversity_matriz)
    min_index, [election,totel] = min_DA(X, DA_matrix, seed = seed)
    election_i.append(election)
    totel_i.append(totel)
    X[min_index] = 0
    sol_i.append(X.copy())
    MD_i.append(MD(X, diversity_matriz))
    if verbose:
      if iter_i % plot_int == 0:
        plt.scatter(N[X==0][:,0], N[X==0][:,1], c = "blue", label = "N")
        plt.scatter(N[X == 1][:,0], N[X == 1][:,1], c = "red", label= "X")
        plt.title(f"Iteración {iter_i} MD = {np.round(MD_i[-1],2)}")
        plt.show()
    iter_i += 1
  time_f = time.time()
  if verbose:
    print("------------------------------------------------------------------------")
    print("---------------------------RESULTADOS-----------------------------------")
    print("------------------------------------------------------------------------")
    print("Vector X: ", X)
    print("MD: ", MD_i[-1])
    print("Tiempo: ", time_f - time_i)
    plt.title(f"Solución final MD = {np.round(MD_i[-1],2)}")
    plt.scatter(N[X==0][:,0], N[X==0][:,1], c = "blue", label = "N")
    plt.scatter(N[X == 1][:,0], N[X == 1][:,1], c = "red", label= "M")
    plt.legend()
    plt.show()
  data = {"MD_ev":MD_i, "Elección":election_i, "Total elecciones":totel_i, "Soluciones":sol_i}
  return X, data, diversity_matriz