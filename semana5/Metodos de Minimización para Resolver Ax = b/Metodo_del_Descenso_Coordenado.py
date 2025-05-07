import numpy as np

def descenso_coordenado(A, b, x0=None, tol=1e-6, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    if x0 is None:
        x0 = np.zeros(n)
    else:
        x0 = np.array(x0, dtype=float)

    x = x0.copy()

    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            suma_inf = sum(A[i][j] * x_new[j] for j in range(i))  # x_j^{(j)}
            suma_sup = sum(A[i][j] * x[j] for j in range(i + 1, n))  # x_j^{(0)}
            x_new[i] = (1 / A[i][i]) * (b[i] - suma_inf - suma_sup)

        # Verificación de convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Convergencia alcanzada en {k + 1} iteraciones.")
            return x_new

        x = x_new

    print("No se alcanzó convergencia en el número máximo de iteraciones.")
    return x

# Ejemplo con matriz simétrica definida positiva
A = [[4, 1],
     [1, 3]]
b = [6, 7]
x0 = [0, 0]

# Ejecución
sol = descenso_coordenado(A, b, x0)
print("Solución aproximada:", sol)
