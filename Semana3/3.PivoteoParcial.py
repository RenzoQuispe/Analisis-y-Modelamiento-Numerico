import numpy as np

def gauss_eliminacion(Ab, verbose=False):
    Ab = Ab.astype(float)
    n = Ab.shape[0]

    for i in range(n):
        # Pivoteo parcial
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        if Ab[max_row, i] == 0:
            raise ValueError("El sistema no tiene solución única (pivote cero).")
        Ab[[i, max_row]] = Ab[[max_row, i]]  # Intercambio de filas

        # Normalizamos la fila del pivote
        Ab[i] = Ab[i] / Ab[i, i]

        # Eliminación hacia abajo
        for k in range(i + 1, n):
            Ab[k] -= Ab[k, i] * Ab[i]

        if verbose:
            print(f"Paso {i + 1} - Matriz aumentada:")
            print(np.round(Ab, 4))
            print()

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])

    return x

# Ejemplo de uso
if __name__ == "__main__":
    # Matriz aumentada: [A | b]
    Ab = np.array([
        [2, 2, -1, 3],
        [2, 2, 3, 15],
        [1, -1, 1, 2]
    ])

    print("Resolviendo sistema lineal por el método de Gauss...\n")
    solucion = gauss_eliminacion(Ab, verbose=True)
    print("Solución del sistema:", np.round(solucion, 4))
