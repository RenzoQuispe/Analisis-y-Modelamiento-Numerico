import numpy as np

'''
El método de Crout es una técnica de factorización LU que
permite resolver sistemas de ecuaciones lineales de la forma:
Ax = b
Se descompone la matriz A como:
A = LU
donde:
▶ L: matriz triangular inferior. En el caso que A sea invertible,
los elementos de la diagonal son no nulos.
▶ U: matriz triangular superior (con unos en la diagonal).
Una vez obtenida la factorización A = LU, se resuelve:
Ly = b(sustitución hacia adelante)
Ux = y(sustitución hacia atrás)
'''
def crout_3x3(A, b):
    n = 3
    L = np.zeros((n, n))
    U = np.identity(n)

    # Factorización LU (Crout)
    for j in range(n):
        for i in range(j, n):
            sum_L = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = A[i][j] - sum_L
        for i in range(j + 1, n):
            sum_U = sum(L[j][k] * U[k][i] for k in range(j))
            U[j][i] = (A[j][i] - sum_U) / L[j][j]

    # Sustitución hacia adelante (Ly = b)
    y = np.zeros(n)
    for i in range(n):
        sum_y = sum(L[i][k] * y[k] for k in range(i))
        y[i] = (b[i] - sum_y) / L[i][i]

    # Sustitución hacia atrás (Ux = y)
    x = np.zeros(n)
    for i in reversed(range(n)):
        sum_x = sum(U[i][k] * x[k] for k in range(i + 1, n))
        x[i] = y[i] - sum_x

    return x, L, U

# Datos
A = np.array([
    [2, 3, 1],
    [4, 7, 7],
    [-2, 4, 5]
], dtype=float)

b = np.array([1, 3, 4], dtype=float)

x, L, U = crout_3x3(A, b)

print("Solución x:\n", x)
print("\nMatriz L:\n", L)
print("\nMatriz U:\n", U)
