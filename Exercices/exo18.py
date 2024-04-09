# Comment remplacer les éléments d'un tableau NumPy qui sont supérieurs à un certain seuil par 0 ?

import numpy as np

tab = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tab[tab > 5] = 0
print(tab)