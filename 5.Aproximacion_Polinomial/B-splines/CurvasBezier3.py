import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from scipy.interpolate import BSpline

# ---------------------------
# FUNCIONES
# ---------------------------

# Bézier con fórmula de Bernstein
def bezier_curve(control_pts, t_vals):
    n = len(control_pts) - 1
    curve = np.zeros((len(t_vals), 2))
    for i in range(n + 1):
        bernstein = comb(n, i) * (1 - t_vals)**(n - i) * t_vals**i
        curve += np.outer(bernstein, control_pts[i])
    return curve

# ---------------------------
# PUNTOS DE CONTROL
# ---------------------------

control_points = np.array([
    [0.0, 0.0],
    [0.2, 1.0],
    [0.8, -1.0],
    [1.0, 0.0]
])

x_ctrl = control_points[:, 0]
y_ctrl = control_points[:, 1]

# ---------------------------
# BÉZIER
# ---------------------------

t_vals = np.linspace(0, 1, 300)
bezier = bezier_curve(control_points, t_vals)

# ---------------------------
# B-SPLINE (cúbica, mismos puntos)
# ---------------------------

k = 3  # grado cúbico
# Vector de nudos para B-spline (mínimo válido: 2*k + 2 - n)
t_bspl = np.concatenate(([0]*k, [0.3, 0.7], [1]*k))  # con nodos internos para suavidad

spl_x = BSpline(t_bspl, x_ctrl, k)
spl_y = BSpline(t_bspl, y_ctrl, k)

bspline = np.vstack((spl_x(t_vals), spl_y(t_vals))).T

# ---------------------------
# GRAFICAR
# ---------------------------

plt.figure(figsize=(10, 5))
plt.plot(bezier[:, 0], bezier[:, 1], 'b-', label='Curva Bézier')
plt.plot(bspline[:, 0], bspline[:, 1], 'g--', label='Curva B-spline')
plt.plot(x_ctrl, y_ctrl, 'ro--', label='Puntos de control')

plt.title("Comparación: Bézier vs B-spline (grado 3)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.tight_layout()
plt.show()
