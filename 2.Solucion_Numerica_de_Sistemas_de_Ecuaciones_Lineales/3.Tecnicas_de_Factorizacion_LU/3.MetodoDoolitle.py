'''
▶ Es una técnica para descomponer una matriz A como el
producto de una matriz triangular inferior L y una triangular
superior U: A = LU
▶ En Doolittle, la matriz L tiene unos en la diagonal.
▶ Esta descomposición se usa para resolver sistemas de
ecuaciones Ax = b.
Una vez obtenida la factorización A = LU, se resuelve:
Ly = b(sustitución hacia adelante)
Ux = y(sustitución hacia atrás)
Conclusión
▶ El método de Doolittle permite resolver sistemas lineales
eficientemente.
▶ Evita operaciones con fracciones en la matriz L gracias a la
diagonal unitaria.
▶ Es una base fundamental en álgebra lineal numérica.
'''
import numpy as np

def doolittle(A):
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
        
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
    
    return L, U

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)
    
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))
    
    return y

def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)
    
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(U[i, j] * x[j] for j in range(i + 1, n))) / U[i, i]
    
    return x

# Datos
A = np.array([
    [1, 2, 1],
    [-1, -3, 0],
    [2, 5, 3]
], dtype=float)

b = np.array([8, -7, 21], dtype=float)

# Factorización y solución
L, U = doolittle(A)
y = forward_substitution(L, b)
x = backward_substitution(U, y)

# Resultados
print("Matriz L:\n", L)
print("Matriz U:\n", U)
print("Solución x:\n", x)
