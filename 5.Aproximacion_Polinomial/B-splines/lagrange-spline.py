import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Función problemática de Runge
def f(x):
    return 1 / (1 + 25 * x**2)

# Generar puntos equidistantes
x_puntos = np.linspace(-1, 1, 11)
y_puntos = f(x_puntos)

# Interpolación Lagrange manual
def lagrange_manual(x_eval, x_nodes, y_nodes):
    total = 0
    n = len(x_nodes)
    for i in range(n):
        xi, yi = x_nodes[i], y_nodes[i]
        li = 1
        for j in range(n):
            if j != i:
                li *= (x_eval - x_nodes[j]) / (xi - x_nodes[j])
        total += yi * li
    return total

# Evaluar lagrange en todos los puntos
x_fina = np.linspace(-1, 1, 1000)
y_real = f(x_fina)
y_lagrange = np.array([lagrange_manual(x, x_puntos, y_puntos) for x in x_fina])

# Interpolación Spline cúbico
spline = CubicSpline(x_puntos, y_puntos)
y_spline = spline(x_fina)

# Errores
mse_lagrange = np.mean((y_real - y_lagrange)**2)
mse_spline = np.mean((y_real - y_spline)**2)

print(f"Error cuadrático medio (Lagrange): {mse_lagrange:.8f}")
print(f"Error cuadrático medio (Spline cúbico): {mse_spline:.8f}")

# Gráfica
plt.figure(figsize=(12,6))
plt.plot(x_fina, y_real, 'k--', label='f(x) = 1 / (1 + 25x²)', linewidth=2)
plt.plot(x_fina, y_lagrange, 'r-', label='Interpolación Lagrange (manual)')
plt.plot(x_fina, y_spline, 'b-', label='Spline cúbico')
plt.plot(x_puntos, y_puntos, 'ko', label='Puntos base')
plt.title('Comparación: Lagrange (manual) vs Spline cúbico\n(fenómeno de Runge)', fontsize=14)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
