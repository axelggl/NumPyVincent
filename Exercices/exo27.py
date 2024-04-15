# Comment calculer la distance euclidienne entre deux tableaux NumPy A et B sans utiliser de boucle ?

import numpy as np

A = np.random.rand(5,5)
B = np.random.rand(5,5)
print("==== Matrice A ====")
print(A)
print("==== Matrice B ====")
print(B)
dist = np.linalg.norm(A - B)
print("==== Distance euclidienne ====")
print(dist)