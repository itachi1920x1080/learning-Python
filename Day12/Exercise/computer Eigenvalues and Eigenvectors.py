import numpy as np
a = np.array ([[1,0],[0,1]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(f'eigenvalues : {eigenvalues}')
print(f'eigenvectors : {eigenvectors}')
