import numpy as np
'''
Método de Descenso por Coordenadas (Coordinate Descent)
    Idea principal: Optimiza una variable a la vez, manteniendo las demás fijas.
    Aplicación típica: Minimización de funciones multivariables, especialmente si son separables o tienen estructura dispersa.
    Iteración: Se selecciona una dirección coordenada (por ejemplo, el eje x1x1​, luego x2x2​, etc.) y se realiza una búsqueda en línea solo sobre esa coordenada.
    Ventaja: Muy eficiente si cada subproblema unidimensional es fácil de resolver.
    Desventaja: Puede ser lento en converger si las variables están muy acopladas (alta dependencia entre coordenadas).

Método de Descenso Relajado (o relajación sucesiva, como en Gauss-Seidel con relajación)
    Idea principal: Es una mejora del método de Gauss-Seidel en la que se mezcla el valor antiguo y el nuevo de la variable actual mediante un parámetro de relajación ωω.
    Aplicación típica: Resolución de sistemas lineales, especialmente en métodos como SOR (Successive Over-Relaxation).
    Ventaja: Mejora la velocidad de convergencia ajustando ωω adecuadamente.
    Desventaja: Requiere buena elección de ωω; si es inadecuado puede ralentizar la convergencia o incluso hacer que diverja.
    Condiciones:
    - Se aplica a sistemas lineales Ax=b.
    - La matriz A debe ser:
        Simétrica definida positiva (óptimo)
        Diagonalmente dominante (suficiente)
    - Es una mejora sobre Gauss-Seidel, usando un parámetro de relajación ω∈(0,2)
    
Conclusion
▶ El parametro de relajacion ω puede acelerar o estabilizar el metodo.
▶ El descenso coordenado es simple, pero puede ser lento en problemas mal condicionados.
▶ Ambos metodos tienen su lugar dependiendo de la estructura del problema.
'''
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
