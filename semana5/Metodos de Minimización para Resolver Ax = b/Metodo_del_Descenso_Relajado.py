import numpy as np

def Q(x, A, b):
    return 0.5 * x.T @ A @ x - b.T @ x

def grad_Q(x, A, b):
    return A @ x - b

def metodo_descenso_relajado(A, b, x0, omega=1.0, tol=1e-6, max_iter=100):
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
        Ap = A @ p
        alpha_hat = (grad.T @ grad) / (p.T @ Ap)
        alpha = omega * alpha_hat
        x = x + alpha * p
        history.append(x.copy())

    else:
        print("No se alcanzó la convergencia en el número máximo de iteraciones.")
    
    return x, np.array(history)

# Definición del problema
A = np.array([[3, 1], [1, 2]])
b = np.array([1, 1])
x0 = np.array([0.0, 0.0])
omega = 1.5

# Ejecución
sol, traj = metodo_descenso_relajado(A, b, x0, omega)

# Resultados
print("Solución aproximada:", sol)
print("Valor mínimo de Q(x):", Q(sol, A, b))
