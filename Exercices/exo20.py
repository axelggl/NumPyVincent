# Comment effectuer une opération de multiplication matricielle entre deux tableaux NumPy ?

import numpy as np

tab1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tab2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
result = np.dot(tab1, tab2)
print(result)