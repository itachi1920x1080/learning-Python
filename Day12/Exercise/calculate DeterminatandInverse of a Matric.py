import numpy as np
a = np.array ([[1,1,1],[1,2,3],[1,4,5]])
determinant = np.linalg.det(a)
inverse = np.linalg.inv(a)
print(f'determinat : {determinant}')
print(f'inverse : {inverse}')