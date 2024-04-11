# Créez un tableau 2D de formes (5,5) rempli de valeurs aléatoires et normalisez-le (soustrayez la moyenne et divisez par l'écart type).

import numpy as np

tab = np.random.rand(5,5)
print("==== Matrice 5x5 ====")
print(tab)
mean = np.mean(tab)
std = np.std(tab)
tab = (tab - mean) / std
print("==== Matrice 5x5 normalisée ====")
print(tab)
