# Comment calculer la moyenne des éléments d'un tableau NumPy ?

import numpy as np

tab = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(tab.mean())
print(np.mean(tab))
print(tab.sum() / tab.size)
print(np.average(tab))