# Comment appliquer une fonction personnalisée à chaque élément d'un tableau NumPy ?

import numpy as np

def custom_function(x):
    return 2 * x + 1

array = np.array([1, 2, 3, 4, 5])
vectorized_function = np.vectorize(custom_function)
result_array = vectorized_function(array)

print("==== Tableau initial ====")
print(array)
print("==== Tableau après application de la fonction ====")
print(result_array)