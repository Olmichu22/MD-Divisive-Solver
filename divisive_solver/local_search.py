from .extra_functions import ordenar_indices, swap
from .reward_functions import MD, DA

def local_search_MA(X, D, j_eval, k_eval, verbose = False): 
    # Calcular DA(X) para la solución dada y ordenar por valor descendente
    da_values = DA(X, D)
    sorted_indices_out = ordenar_indices(da_values, X, True, False)
    sorted_indices_in = ordenar_indices(da_values, X, False, True)

    j = 0
    mejora = False
    limite_k = j_eval
    limite_j = k_eval
    # Bucle de búsqueda local
    while not mejora and j <= limite_j and j < len(sorted_indices_out):
    # Seleccionar el j-ésimo elemento máximo (ejemplo: por mayor DA)
        j_index = sorted_indices_out[j]
        k = 0
        while not mejora and k <= limite_k and k < len(sorted_indices_in):
            # Seleccionar el k-ésimo elemento mínimo (ejemplo: por menor DA)
            k_index = sorted_indices_in[k]            
            # Intentar un swap
            X_star = swap(X, j_index, k_index)
            # print(X_star)            
            if MD(X, D) < MD(X_star, D):
              mejora = True
            k += 1
        j += 1
    if verbose:
      print("Número de iteraciones: ", j*k)
      print("Solución inicial: ", X)
      print("Valor de MD inicial: ", MD(X, D))
      print("Solución final: ", X_star)
      print("Valor de MD final: ", MD(X_star, D))
      print(f"Posiciones intercambiadas,  {j_index} entra y {k_index} sale")
      print(f"Se cumple condicion {MD(X_star, D)}>{MD(X, D)}")
      print(f"La diferenca de MD es {MD(X_star, D)-MD(X, D)}")
    return X_star, mejora