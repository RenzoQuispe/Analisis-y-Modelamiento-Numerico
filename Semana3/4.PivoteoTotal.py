'''
Objetivo:
Mejorar la estabilidad aún más que el pivoteo parcial,
intercambiando filas y columnas para colocar el pivote más
adecuado y minimizar el error de redondeo.

Algortimo:
Para cada paso k:
1. Seleccionar el pivote: Buscar el elemento máximo en valor
absoluto (pivote) en el submatriz restante Ak:n,k:n .
2. Intercambiar filas y columnas: Despúes de seleccionar el
pivote, intercambiamos filas y columnas para colocar ese
elemento en la posición akk .
3. Eliminación Gaussiana: Realizamos las operaciones de Gauss
para transformar la matriz A en una forma triangular superior.
4. Reordenar incógnitas: Luego de la sustitución regresiva, se
reordena las incógnitas debido al intercambio de columnas.
'''
import numpy as np

def pivoteo_total(A, b):
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)
    marcas = list(range(n))  # Para rastrear el orden original de las columnas

    for k in range(n - 1):
        # Buscar el máximo en el subbloque A[k:n, k:n]
        submatriz = np.abs(A[k:n, k:n])
        i_max, j_max = divmod(np.argmax(submatriz), n - k)
        i_max += k
        j_max += k

        # Intercambiar filas
        if i_max != k:
            A[[k, i_max], :] = A[[i_max, k], :]
            b[k], b[i_max] = b[i_max], b[k]

        # Intercambiar columnas (y marcas)
        if j_max != k:
            A[:, [k, j_max]] = A[:, [j_max, k]]
            marcas[k], marcas[j_max] = marcas[j_max], marcas[k]

        # Eliminación hacia abajo
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    # Sustitución regresiva
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

    # Reordenar resultados según marcas
    x_final = np.zeros(n)
    for i in range(n):
        x_final[marcas[i]] = x[i]

    return np.round(x_final, 4)

# Datos del sistema
A = np.array([
    [2, 2, -1],
    [2, 2, 3],
    [1, -1, 1]
])
b = np.array([3, 15, 2])

sol = pivoteo_total(A, b)

print("Solución del sistema:")
for i, val in enumerate(sol, 1):
    print(f"x{i} = {val}")

