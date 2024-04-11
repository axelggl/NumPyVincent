# Calculez le déterminant d'une matrice 3x3.

import numpy as np

# tableau 3x3 avec des valeurs aléatoires
tab = np.random.rand(3,3)
det = np.linalg.det(tab)
print(tab)
print(det)