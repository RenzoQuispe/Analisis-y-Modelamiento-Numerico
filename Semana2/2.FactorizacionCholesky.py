import numpy as np
from numpy.linalg import cholesky
'''
Si A es *simétrica* y *definida positiva*, entonces existe:
A = LL^T
donde L es triangular inferior con entradas reales positivas en la
diagonal. Más eficiente que LU en este caso.
Para que exista la factorización de Cholesky:
▶ A = AT (simetria)
▶ x^T Ax > 0 para todo x != 0 (definida positiva). Tambien autovalores positivos o determinantes de principales mayores a cero
'''
A = np.array([[4, 2], [2, 3]])
L = cholesky(A)

print("L =\n", L)
print("LL^T =\n", L @ L.T)
