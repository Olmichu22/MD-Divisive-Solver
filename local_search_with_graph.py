from divisive_solver.heuristic import MD_problem_heuristic
import numpy as np
from divisive_solver.local_search import  local_search_MA_animated

n_points = 1000
mean = 0
std_dev = 5
np.random.seed(0)
# Generar n_points puntos aleatorios de una normal de media 0 y desviacion std de dimensión 2
N = np.random.normal(mean, std_dev, size=(n_points, 2))
# N = np.random.randn(0,20, size= (n_points,2))
M_dim = 50
X, data, Da_m = MD_problem_heuristic(N, M_dim, 1, verbose = False)
local_search_MA_animated(X, Da_m, N, n_points-np.sum(X), np.sum(X)-1, verbose = True)
