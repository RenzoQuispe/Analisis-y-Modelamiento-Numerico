import numpy as np
'''
Metodo de Gauss-Seidel:
▶ Usa los valores mas recientes disponibles durante la iteracion.
▶ Converge mas rapido que Jacobi en general
▶ Gauss-Seidel mejora a Jacobi usando actualizaciones inmediatas.
'''
def gauss_seidel(A, b, x0=None, tol=1e-2, max_iter=30):
    n = len(A)
    x = np.zeros_like(b) if x0 is None else x0.copy()

    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            # s1 usa valores ya actualizados en esta iteración
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            # s2 usa valores de la iteración anterior
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        # Verificar convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1
        x = x_new

    raise Exception("El método de Gauss-Seidel no convergió")

# Datos
A = np.array([[4.0, 1.0],
              [2.0, 3.0]])
b = np.array([15.0, 15.0])

# Ejecución
x_aprox, iteraciones = gauss_seidel(A, b)
print("Solución aproximada:", x_aprox)
print("Iteraciones:", iteraciones)
