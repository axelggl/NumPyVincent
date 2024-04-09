# Créez une matrice 5x5 avec des valeurs 1,2,3,4 juste en dessous de la diagonale.

import numpy as np

tab = np.diag([1, 2, 3, 4], k=-1)
print(tab)
