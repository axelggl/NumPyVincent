# Créez un tableau 2D représentant un plan d'échiquier (8x8), où les cases alternent entre 0 (blanc) et 1 (noir).

import numpy as np

tab = np.zeros((8,8), dtype=int)
print("==== Plan d'échiquier ====")
print(tab)
tab[1::2, ::2] = 1
print("==== Plan d'échiquier avec le quart des cases alternées ====")
print(tab)
tab[::2, 1::2] = 1
print("==== Plan d'échiquier avec la moitié des cases alternées ====")
print(tab)