import numpy as np
from scipy.linalg import lu

# Factorizacion LU para A
'''
Pivoteo parcial: Intercambia filas de la matriz.
Pivoteo completo: Intercambia filas y columnas.
PA = LU
si A permite eliminacion sin pivoteo (intercambio de filas) entonces P = I 

LU: se aplica a cualquier matriz cuadrada (sin pivoteo en la teoria).
'''
A = np.array([[-2, 4, -1], [4, -5, 4],[-6,-3,-14]])
P, L, U = lu(A)
print("P =\n", P)
print("L =\n", L)
print("U =\n", U)


def lu_factorization(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        # Calcular U
        for j in range(i, n):
            suma = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - suma
        
        # Calcular L
        for j in range(i, n):
            if i == j:
                L[i][i] = 1
            else:
                suma = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (A[j][i] - suma) / U[i][i]
    
    return L, U


'''
import numpy as np
from scipy.linalg import lu
A = np.array([[2 , 3] , [4 , 7]])
P , L , U = lu(A)
print ( " L =\n " , L )
print ( " U =\n " , U )
'''