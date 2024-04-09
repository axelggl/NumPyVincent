# Comment trouver les indices des éléments non nuls dans un tableau NumPy ?

import numpy as np

tab = np.array([[1, None, 3], [None, 5, None], [7, None, 9]])
indices = np.argwhere(tab != None)
print(indices)