import numpy as np

# Definir la matriz aumentada A | b
A = np.array([
    [-1, 3, -1, 1],
    [1, -1, 2, 2],
    [3, 1, -2, 2]
], dtype=float)

# Función para realizar eliminación de Gauss sin pivoteo
def gauss_elimination(A):
    rows, cols = A.shape

    # Paso 1: Triangularización
    for i in range(rows):
        for j in range(i + 1, rows):
            if A[j, i] != 0:  # Si el coeficiente no es cero
                factor = A[j, i] / A[i, i]
                A[j] = A[j] - factor * A[i]
    
    # Paso 2: Sustitución hacia atrás
    x = np.zeros(rows)
    for i in range(rows - 1, -1, -1):
        x[i] = (A[i, -1] - np.dot(A[i, i + 1:rows], x[i + 1:])) / A[i, i]
    
    return x

# Aplicar eliminación de Gauss
solution = gauss_elimination(A)

# Mostrar la solución
print("La solución del sistema es:")
for i in range(len(solution)):
    print(f"x{i + 1} = {solution[i]}")
