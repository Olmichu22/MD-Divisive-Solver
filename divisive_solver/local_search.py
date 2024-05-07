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
      if mejora:
        print("Número de iteraciones: ", j * k)
        print("Solución inicial: ", X)
        print("Valor de MD inicial: ", MD(X, D))
        print("Solución final: ", X_star)
        print("Valor de MD final: ", MD(X_star, D))
        print(f"Posiciones intercambiadas, {j_index} entra y {k_index} sale")
        print(f"Se cumple condición {MD(X_star, D) > MD(X, D)}")
        print(f"La diferencia de MD es {MD(X_star, D) - MD(X, D)}")
      else:
        print("No se encontró mejora")
    return X_star, mejora
  
import matplotlib.pyplot as plt
import numpy as np
import time

def local_search_MA_animated(X, D, n, j_eval, k_eval, verbose=False):
    da_values = DA(X, D)
    sorted_indices_out = ordenar_indices(da_values, X, False, False)
    sorted_indices_in = ordenar_indices(da_values, X, True, True)
    # print(X)
    # print(sorted_indices_out)
    # print(sorted_indices_in)
    j = 0
    mejora = False
    limite_k = j_eval
    limite_j = k_eval

    # Configuración inicial de la visualización
    plt.ion()
    fig, ax = plt.subplots()
    positions = np.array([n[i][:2] for i in range(len(n))])  # Usar las dos primeras dimensiones de n para posiciones
    
    # Colores iniciales para todos los puntos
    colors = ['lightgray' if x == 0 else 'red' for x in X]
    sc = ax.scatter(positions[:, 0], positions[:, 1], color=colors)
    ax.set_title('Estado inicial')
    plt.draw()
    plt.pause(2)  # Pausa antes de iniciar

    while not mejora and j <= limite_j and j < len(sorted_indices_out):
        j_index = sorted_indices_out[j]
        k = 0
        while not mejora and k <= limite_k and k < len(sorted_indices_in):
            k_index = sorted_indices_in[k]
            X_star = swap(X, j_index, k_index)

            # Colores actualizados para la visualización
            colors = ['lightgray'] * len(X)
            for i in range(len(X)):
                if X_star[i] == 1:
                    colors[i] = 'red'
            colors[j_index] = 'blue'  # Color azul para el punto de intercambio exterior
            colors[k_index] = 'green' # Color verde para el punto susceptible de ser intercambiado

            sc.set_color(colors)
            ax.set_title(f'Intentando swap: {j_index} <-> {k_index}')
            plt.draw()
            plt.pause(0.01)  # Tiempo de pausa para visualización

            if MD(X, D) < MD(X_star, D):
                mejora = True

            k += 1
        j += 1

    plt.ioff()
    ax.legend(handles=[
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgray', markersize=10, label='No seleccionado'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Seleccionado'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Susceptible de intercambio'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Punto de intercambio exterior')
    ])
    ax.set_title('Estado final')
    plt.show()


    if verbose:
      if mejora:
        print("Número de iteraciones: ", j * k)
        print("Solución inicial: ", X)
        print("Valor de MD inicial: ", MD(X, D))
        print("Solución final: ", X_star)
        print("Valor de MD final: ", MD(X_star, D))
        print(f"Posiciones intercambiadas, {j_index} entra y {k_index} sale")
        print(f"Se cumple condición {MD(X_star, D) > MD(X, D)}")
        print(f"La diferencia de MD es {MD(X_star, D) - MD(X, D)}")
      else:
        print("No se encontró mejora")
    return X_star, mejora