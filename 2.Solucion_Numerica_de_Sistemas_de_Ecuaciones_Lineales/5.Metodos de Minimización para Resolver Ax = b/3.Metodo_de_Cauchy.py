import numpy as np

def Q(x, A, b):
    return 0.5 * x.T @ A @ x - b.T @ x

def grad_Q(x, A, b):
    return A @ x - b

def metodo_cauchy(A, b, x0, tol=1e-6, max_iter=100):
    x = x0.copy()
    history = [x.copy()]

    for k in range(max_iter):
        grad = grad_Q(x, A, b)
        
        # Verificar convergencia
        if np.linalg.norm(grad) < tol:
            print(f"Convergencia alcanzada en {k + 1} iteraciones.")
            break

        # Actualización de x
        p = -grad
        alpha = (grad.T @ grad) / (p.T @ A @ p)
        x = x + alpha * p
        history.append(x.copy())

    else:
        print("No se alcanzó la convergencia en el número máximo de iteraciones.")
    
    return x, np.array(history)

# Definición del problema
A = np.array([[3, 1], [1, 2]])
b = np.array([1, 1])
x0 = np.array([0.0, 0.0])

# Ejecución
traj_cauchy, iters_cauchy = metodo_cauchy(A, b, x0)

# Resultados
print("Solución aproximada:", traj_cauchy)
print("Valor mínimo de Q(x):", Q(traj_cauchy, A, b))

'''
Método de Cauchy (Descenso por Gradiente)

Condiciones:
- La función debe ser:
    Diferenciable
    Convexa (para garantizar convergencia al mínimo global)
- Si la función es cuadrática: f(x) = ½x^TAx − b^Tx
    A debe ser simétrica definida positiva.
- Se requiere una búsqueda de línea para determinar la longitud del paso óptima en cada iteración.
'''