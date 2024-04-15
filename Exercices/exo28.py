# Comment trouver les éléments communs entre deux tableaux NumPy ? gg

import numpy as np

A = np.random.randint(0, 10, 10)
B = np.random.randint(0, 10, 10)
print("==== Tableau A ====")
print(A)
print("==== Tableau B ====")
print(B)
print("==== Elements communs ====")
print(np.intersect1d(A, B))
