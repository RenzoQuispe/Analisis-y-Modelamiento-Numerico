import numpy as np

def broyden_inverse_update(B_inv, d, u, tol=1e-12):
    """
    Actualiza la inversa del Jacobiano aproximado usando la fórmula de Broyden (Sherman-Morrison).
    """
    Bd_u = B_inv @ u
    dT_Bd_u = d.T @ Bd_u

    if np.abs(dT_Bd_u) < tol:
        raise ValueError("Denominador en la fórmula de Sherman-Morrison es muy pequeño.")

    correction = np.outer((d - Bd_u), d.T @ B_inv) / dT_Bd_u
    return B_inv + correction


def broyden_method(F, x0, max_iter=50, tol=1e-8, verbose=True):
    """
    Método de Broyden con actualización de la inversa del Jacobiano (Sherman-Morrison).
    
    Parámetros:
    - F: función no lineal vectorial
    - x0: vector inicial
    - max_iter: máximo número de iteraciones
    - tol: tolerancia para detener la iteración
    - verbose: si True, imprime cada iteración

    Retorna:
    - x: vector solución
    - history: lista con los puntos visitados
    """
    x = np.array(x0, dtype=float)
    n = len(x)
    B_inv = np.eye(n)
    fx = F(x)
    history = [x.copy()]

    for k in range(max_iter):
        dx = -B_inv @ fx
        x_new = x + dx
        fx_new = F(x_new)

        if norm := np.linalg.norm(fx_new) < tol:
            if verbose:
                print(f"Convergencia en iteración {k}: ||F(x)|| < {tol}")
            return x_new, history

        try:
            B_inv = broyden_inverse_update(B_inv, dx, fx_new - fx)
        except ValueError as e:
            print(f"Iteración {k}: {e}")
            break

        x = x_new
        fx = fx_new
        history.append(x.copy())

        if verbose:
            print(f"Iter {k:2d}: x = {x}, ||F(x)|| = {np.linalg.norm(fx):.2e}")

    print("No convergió en", max_iter, "iteraciones.")
    return x, history

def F(x):
    return np.array([
        2 * x[0] + 2 * x[1] - 4,
        x[0] * np.exp(x[1]) - 1
        #x[0]**2 - 10*x[0] + x[1]**2 + 8,
        #x[0]*x[1]**2 + x[0] - 10*x[1] + 8
        #x[0]**2 + x[1]**2 - 4,
        #np.exp(x[0]) + x[1] - 1        
    ])

x0 = np.array([3.0, -1.0])
#x0 = np.array([2.0, 3.0])
sol, hist = broyden_method(F, x0)

print("\nSolución encontrada:", sol)
print("F(x) en la solución:", F(sol))