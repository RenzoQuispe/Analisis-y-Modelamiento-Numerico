import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Matriz A
A = np.array([[4, 1, 0],
              [1, 3, 1],
              [0, 1, 2]], dtype=float)

# Vector inicial x0 (no nulo)
x = np.array([1.0, 0.0, 0.0])

# Tolerancia y número máximo de iteraciones
tol = 1e-6
max_iter = 100

# Factorización LU de A (no se calcula la inversa)
lu, piv = lu_factor(A)

k = 0
while True:
    k += 1

    # Paso 1: resolver A * x_hat = x
    x_hat = lu_solve((lu, piv), x)

    # Paso 2: normalizar con el valor absoluto máximo
    mu = np.max(np.abs(x_hat))
    x_new = x_hat / mu

    # Condición de convergencia
    if np.linalg.norm(x_new - x, ord=np.inf) < tol or k >= max_iter:
        break

    # Actualizar x
    x = x_new

    print(f"Iteración {k}: μ ≈ {mu:.6f}, x ≈ {x}")

# Mostrar resultado final
lambda_min_aprox = 1 / mu
print("\nResultado final:")
print(f"Autovalor de menor magnitud aproximado: {lambda_min_aprox:.6f}")
print(f"Autovector aproximado (normalizado): {x_new}")