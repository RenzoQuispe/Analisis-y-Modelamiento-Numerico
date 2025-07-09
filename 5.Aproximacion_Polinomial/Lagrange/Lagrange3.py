import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x):
    total = 0
    n = len(x_points)
    for i in range(n):
        xi, yi = x_points[i], y_points[i]
        Li = 1
        for j in range(n):
            if j != i:
                xj = x_points[j]
                Li *= (x - xj) / (xi - xj)
        total += yi * Li
    return total

# Definir nodos equidistantes en [0, pi]
nodos = np.linspace(0, np.pi, 5)
valores = np.sin(nodos)

# Evaluar el polinomio en un rango denso para graficar
#x_fino = np.linspace(0, np.pi, 200)
x_fino = np.linspace(-1.5, 4.5, 200)

y_interpolado = [lagrange_interpolation(nodos, valores, x) for x in x_fino]

# Función original para comparación
y_original = np.sin(x_fino)

# Graficar
plt.figure(figsize=(8,5))
plt.plot(x_fino, y_original, label='sin(x) (función original)', color='green')
plt.plot(x_fino, y_interpolado, label='Polinomio de Lagrange', color='blue', linestyle='--')
plt.scatter(nodos, valores, color='red', label='Nodos (puntos de interpolación)')
plt.title('Interpolación de sin(x) con Polinomio de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
