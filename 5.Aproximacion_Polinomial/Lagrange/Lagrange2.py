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

# Datos originales
x_pts = [1, 2, 4]
y_pts = [2, 3, 1]

# Crear un rango de valores x para graficar el polinomio interpolador
x_vals = np.linspace(min(x_pts) - 1, max(x_pts) + 1, 200)
y_vals = [lagrange_interpolation(x_pts, y_pts, x) for x in x_vals]

# Graficar
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="Polinomio de Lagrange", color='blue')
plt.scatter(x_pts, y_pts, color='red', label="Puntos originales", zorder=5)
plt.title("Interpolación usando Polinomio de Lagrange")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
