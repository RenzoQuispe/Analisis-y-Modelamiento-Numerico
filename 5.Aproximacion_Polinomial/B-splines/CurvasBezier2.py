import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

# Definir los puntos de control (puedes moverlos para probar)
control_points = np.array([
    [0.0, 0.0],
    [0.2, 0.9],
    [0.8, -0.6],
    [1.0, 0.0]
])

# Número de puntos de control y grado
n = len(control_points) - 1  # Grado = número de puntos - 1

# Función que calcula la curva Bézier usando polinomios de Bernstein
def bezier_curve(control_pts, t_vals):
    n = len(control_pts) - 1
    curve = np.zeros((len(t_vals), 2))
    for i in range(n + 1):
        bernstein_poly = comb(n, i) * (1 - t_vals) ** (n - i) * t_vals ** i
        curve += np.outer(bernstein_poly, control_pts[i])
    return curve

# Evaluar la curva
t = np.linspace(0, 1, 300)
bezier_pts = bezier_curve(control_points, t)

# Graficar
plt.figure(figsize=(8, 5))
plt.plot(bezier_pts[:, 0], bezier_pts[:, 1], 'b-', label='Curva Bézier')
plt.plot(control_points[:, 0], control_points[:, 1], 'ro--', label='Puntos de control')
plt.title('Curva de Bézier (cúbica)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
