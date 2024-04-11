# Inverser une matrice 3x3.

import numpy as np

tab = np.array([[4, 10, 7], [4, 1, 3], [10, 12, 14]])
print("==== Matrice 3x3 ====")
print(tab)
print("==== Inversée ====")
inv = np.linalg.inv(tab)
print(inv)