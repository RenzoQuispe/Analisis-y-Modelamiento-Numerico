import numpy as np
from scipy.linalg import lu_factor, lu_solve
""" METODO POTENCIA INVERSA DESPLAZADO
▶ Queremos encontrar λk (mas cercano a µ ∈ C) tal que
    0 < |λk - µ| < ε,
y todos los otros autovalores λj , cumplen
    |λj - µ| > ε.
▶ Consideramos la matriz desplazada
    A - µI.
▶ Aplicamos el metodo de potencia inversa a A - µI:
    (A - µI)x^(k+1) = x^(k)
▶ Al converger,
z = 1/(λk - µ)  => λk = µ + 1/z
▶ Queremos encontrar λk (mas lejano a µ ∈ C) tal que
    |λk - µ| > ε,
y para otros autovalores λj,
    0 < |λj - µ| < ε.
▶ Aplicamos el metodo de potencia a A - µI:
    x^(k+1) = (A - µI)x^(k)
▶ Al converger, el cociente de Rayleigh aproxima z = λk - µ:
    λk = µ + z.
"""
def potencia_inversa_desplazada(A, mu, x0=None, tol=1e-10, max_iter=1000):
    n = A.shape[0]
    I = np.eye(n)
    A_shifted = A - mu * I

    # Factorización LU una sola vez para eficiencia
    lu, piv = lu_factor(A_shifted)

    # Vector inicial aleatorio si no se da uno
    if x0 is None:
        x = np.random.rand(n)
    else:
        x = x0.copy()

    x = x / np.linalg.norm(x)

    for _ in range(max_iter):
        # Resolver (A - mu I) y = x
        y = lu_solve((lu, piv), x)

        # Normalizar
        x_new = y / np.linalg.norm(y)

        # revisar convergencia
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new

    # estimar el autovalor con el cociente de Rayleigh
    z = np.dot(x.T, lu_solve((lu, piv), x))
    lambda_k = mu + 1 / z

    return lambda_k, x

# Matriz de ejemplo
A = np.array([
    [4, 1, 0],
    [1, 3, 1],
    [0, 1, 2]
], dtype=float)

# Valor cercano (mu)
mu = 2.5

# Ejecutar el método
lambda_aprox, autovector = potencia_inversa_desplazada(A, mu)

print("Autovalor aproximado:", lambda_aprox)
print("Autovector aproximado:", autovector)
