import numpy as np

def broyden(F, x0, tol=1e-8, max_iter=100):
    """
    Método de Broyden para resolver F(x) = 0  (Método Cuasi-Newton)
    
    El método de Broyden es un algoritmo numérico utilizado para resolver sistemas de ecuaciones no lineales, y es una alternativa al método de Newton,
    especialmente cuando la evaluación del jacobiano (la matriz de derivadas parciales) es costosa o complicada.

    Parámetros:
    - F: función vectorial (de R^n a R^n)
    - x0: vector inicial
    - tol: tolerancia para la norma del residuo
    - max_iter: número máximo de iteraciones

    Retorna:
    - x: solución aproximada
    - k: número de iteraciones
    """
    """
    - Se usa para resolver sistemas no lineales F(x) = 0 sin calcular el jacobiano exacto.
    - Aproxima el Jacobiano con una actualizacion iterativa.
    - Muy util en problemas donde el Jacobiano es dificil de obtener.
    """

    x = x0.astype(float)
    n = len(x)
    B = np.eye(n)  # Aproximación inicial del Jacobiano
    Fx = F(x)

    for k in range(max_iter):
        try:
            s = np.linalg.solve(B, -Fx)  # Resuelve B s = -F(x)
        except np.linalg.LinAlgError:
            print("Matriz B singular.")
            return x, k

        x_new = x + s
        Fx_new = F(x_new)
        y = Fx_new - Fx
        Bs = B @ s
        B += np.outer((y - Bs), s) / np.dot(s, s)  # Actualización de Broyden

        if np.linalg.norm(Fx_new, ord=2) < tol:
            return x_new, k + 1

        x = x_new
        Fx = Fx_new

    print("No convergió en", max_iter, "iteraciones.")
    return x, max_iter

def F(x):
    return np.array([
        #x[0]**2 + x[1]**2 - 4,
        #np.exp(x[0]) + x[1] - 1
        2 * x[0] + 2 * x[1] - 4,
        x[0] * np.exp(x[1]) - 1
    ])

x0 = np.array([3.0, -1.0])
sol, iterations = broyden(F, x0)

print("Solución:", sol)
print("Iteraciones:", iterations)