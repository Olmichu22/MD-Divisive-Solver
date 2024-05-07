# MD-Divisive-Solver
# Diversity Maximization Library

This library provides tools for solving the Diversity Maximization problem, commonly used in combinatorial optimization to select a subset of items that are as diverse as possible according to certain criteria.

## Problem Description

The Diversity Maximization problem aims to select a subset of elements from a larger set such that the diversity among the selected elements is maximized. Mathematically, given a set \( N \) of \( n \) elements, the goal is to select \( m \) elements that maximize the diversity index, defined based on distances or dissimilarities between the elements.
Diversity could be calculated as follows:

$$
MD(X) = \sum_{i}^{n-1} \sum_{j < i}^n d_{ij}x_ix_j
$$

where $x_i$ and $x_j$ are binary variables indicating if elements $i$ and $j$ are selected, respectively, and $d_{ij}$ is the diversity between elements $i$ and $j$.

Vector $X$ meets the following constraint:

$$
\sum_{i}^{n} x_i = m
$$
## Functions

### `MD_problem_heuristic`

This function implements a heuristic approach to solve the Diversity Maximization problem.

- **Parameters:**
  - `N`: Array of elements.
  - `M_dim`: Number of elements to select.
  - `seed`: Random seed for reproducibility.
  - `verbose`: If `True`, enables the output of detailed iteration data.
  - `D_matrix`: Optional precomputed diversity matrix. If not provided, it is computed internally.
  - `plot_int`: Interval for plotting intermediate results during execution.

- **Returns:**
  - `X`: Binary vector indicating selected elements.
  - `data`: Dictionary with detailed information about the solution process.
  - `diversity_matrix`: Computed or provided matrix of diversity values.

### Distance Functions

#### `D`

Calculates the Euclidean distance matrix for a given set of points.

#### `MD`

Computes the diversity for a given solution \( X \) using a precomputed diversity matrix \( D_matrix \).

#### `DA`

Calculates the diversity contribution of each element in \( X \) based on \( D_matrix \).

#### `min_DA`

Identifies the element of \( X \) that minimizes the diversity contribution to the rest of the elements.

## Local Search Algorithm

The `local_search_MA` function enhances an initial solution by iteratively swapping elements to increase the overall diversity.

- **Parameters:**
  - `X`: Initial solution vector.
  - `D`: Diversity matrix.
  - `j_eval`, `k_eval`: Limits for the number of evaluations in external and internal loops, respectively.
  - `verbose`: Enables detailed output.

- **Returns:**
  - `X_star`: Improved solution.
  - `mejora`: Boolean indicating if an improvement was made.

## Algorithm Pseudocode

### Heuristic for Diversity Maximization

1. Initialize solution vector \( X \) with all elements selected.
2. Compute or use provided diversity matrix.
3. Repeatedly deselect the element minimizing diversity until \( m \) elements remain.
4. Optionally plot intermediate results and print detailed information.

### Local Search

1. Calculate diversity contributions for all elements.
2. Sort indices of elements inside and outside the current solution based on their diversity contributions.
3. Iteratively attempt to swap elements to improve the diversity measure.
4. If an improvement is detected, update the solution.
5. Print iteration details and results if verbose mode is enabled.

## Code Operation

This library makes extensive use of numpy for efficient mathematical operations. It integrates plotting functionality through matplotlib for visual analysis during the heuristic process. The local search function leverages sorted indices to minimize computational overhead during the iterative improvement phase.
