# Utilisez la "fancy indexing" pour extraire des éléments non contigus d'un tableau (par exemple, extraire les éléments aux positions [1, 3, 8]).

import numpy as np

# Creating a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

rows_index = np.array([0, 1, 2])
cols_index = np.array([0, 2, 1])
print("Rows indices:", rows_index) # Récupère les indices des lignes
print("Columns indices:", cols_index) # Récupère les indices des colonnes

selected_elements = arr[rows_index, cols_index]
print("Selected elements using fancy indexing:", selected_elements)

