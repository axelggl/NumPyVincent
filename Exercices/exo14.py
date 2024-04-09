# Comment accéder aux éléments d'un tableau multidimensionnel ?

import numpy as np

tab = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(tab)
print(tab[0][0])
print(tab[2,2])