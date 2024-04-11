# Trouvez les valeurs et vecteurs propres d'une matrice 3x3.

import numpy as np

tab = np.random.rand(3,3)
print("==== Matrice 3x3 ====")
print(tab)
val, vec = np.linalg.eig(tab)
print("Valeurs propres :")
print(val)
print("Vecteurs propres :")
print(vec)