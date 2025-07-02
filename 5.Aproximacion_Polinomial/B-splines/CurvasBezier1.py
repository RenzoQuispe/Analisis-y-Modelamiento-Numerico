import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline
"""
Una curva de Bézier de grado k es idéntica a una B-spline de:
- Grado k y k+1 puntos de control
- Vector de nudos: t=[0,0,…,0,1,1,…,1] (repetido k+1 veces en cada extremo)
- Sin nodos internos
Esto hace que la B-spline se reduzca a una curva Bézier clásica, con las funciones base Bernstein.
"""
# Una curva de Bézier es una B-spline sin nodos internos, con extremos completamente pegados (repetidos), lo que la convierte en un caso global y especial de una B-spline.

# Función objetivo
def f(x):
    return np.sin(2 * np.pi * x) + 0.2 * np.exp(-200 * (x - 0.5)**2)

# Grado de la curva Bézier
k = 3  # cúbica

# Puntos de control desde la función f
bezier_ctrl_x = np.linspace(0, 1, 4)
bezier_ctrl_y = f(bezier_ctrl_x)

# Vector de nudos para Bézier cúbica: [0, 0, 0, 0, 1, 1, 1, 1]
t_bezier = np.concatenate(([0] * (k+1), [1] * (k+1)))

# Crear B-splines separados para X y Y
spl_bx = BSpline(t_bezier, bezier_ctrl_x, k)
spl_by = BSpline(t_bezier, bezier_ctrl_y, k)

# Evaluar la curva Bézier
t_vals = np.linspace(0, 1, 500)
bezier_x = spl_bx(t_vals)
bezier_y = spl_by(t_vals)

# Evaluar la función original
x = np.linspace(0, 1, 500)
y_true = f(x)

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(x, y_true, 'k--', label='Función original f(x)')
plt.plot(bezier_x, bezier_y, 'g-', label='Curva Bézier (4 pts)')
plt.plot(bezier_ctrl_x, bezier_ctrl_y, 'ro--', label='Ptos de control Bézier')
plt.title('Curva Bézier aproximando una función')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
