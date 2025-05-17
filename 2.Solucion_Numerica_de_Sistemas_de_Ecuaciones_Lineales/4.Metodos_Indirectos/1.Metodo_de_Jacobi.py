import numpy as np
'''
Metodo de Jacobi:
▶ Calcula cada nueva componente usando solo valores de la iteracion anterior.
▶ Requiere matriz diagonalmente dominante o simetrica definida positiva.
▶ Facil de paralelizar.

'''
def jacobi(A, b, x0=None, tol=1e-2, max_iter=30):
    n = len(A)
    x = np.zeros_like(b) if x0 is None else x0.copy()

    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        # Verificar convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1
        x = x_new

    raise Exception("El método superó el número máximo de iteraciones para alcanzar la tolerancia")

# Datos
A = np.array([[4.0, 1.0],
              [2.0, 3.0]])
b = np.array([15.0, 15.0])

x_aprox, iteraciones = jacobi(A, b)
print("Solución aproximada:", x_aprox)
print("Iteraciones:", iteraciones)
