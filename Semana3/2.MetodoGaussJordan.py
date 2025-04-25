import numpy as np
'''
Objetivo:
Llevar la matriz aumentada a la forma escalonada reducida
(identidad en la parte izquierda) para obtener la solución directa
sin sustitución.
Algortimo:
1. Aplicar Gauss para obtener una matriz triangular superior.
2. Continuar eliminando hacia arriba para hacer ceros por encima
de los pivotes.
3. Normalizar cada fila dividiéndola por su pivote para que quede
un 1.
'''
# Definir la matriz aumentada A | b
A = np.array([
    [-1, 3, -1, 1],
    [1, -1, 2, 2],
    [3, 1, -2, 2]
], dtype=float)

# Función para aplicar Gauss-Jordan
def gauss_jordan(A):
    rows, cols = A.shape

    # Proceso de eliminación Gauss-Jordan
    for i in range(rows):
        # Hacer que el pivote sea 1 (dividiendo toda la fila)
        A[i] = A[i] / A[i, i]
        # Hacer ceros en la columna del pivote
        for j in range(rows):
            if i != j:
                A[j] = A[j] - A[j, i] * A[i]
    
    return A

# Aplicar Gauss-Jordan
result = gauss_jordan(A)

# Mostrar el resultado de la matriz aumentada reducida
print("Resultado de la matriz aumentada reducida:")
print(result)

# Extraer la solución de las incógnitas (última columna)
sol = result[:, -1]
print("\nSolución:")
print(f"x1 = {sol[0]}")
print(f"x2 = {sol[1]}")
print(f"x3 = {sol[2]}")
