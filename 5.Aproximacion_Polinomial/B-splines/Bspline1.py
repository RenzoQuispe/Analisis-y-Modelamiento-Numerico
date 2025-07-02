import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline, make_lsq_spline
"""
La B-spline es una curva compuesta por tramos polinómicos suaves, 
que se construye para aproximar una función (basada en puntos muestreados) usando pocos parámetros, 
y que puede adaptarse mejor si colocas más nodos donde la función cambia rápido.
Un B-spline de grado n tiene continuidad de derivadas hasta orden C^n-1
"""

# BSpline: permite evaluar funciones B-spline directamente.
# make_lsq_spline: construye una B-spline que aproxima puntos usando mínimos cuadrados.

# Función objetivo a aproximar (con zonas suaves y zonas con mayor curvatura)
def f(x):
    return np.sin(2 * np.pi * x) + 0.2 * np.exp(-200 * (x - 0.5)**2)

# Puntos de evaluación
x = np.linspace(0, 1, 500)
y_true = f(x)

# Grado de la B-spline
k = 3

# Nodos iniciales (uniformes)
n_knots = 8
# Se crean 8 nodos uniformemente distribuidos entre 0 y 1.
knots_uniform = np.linspace(0, 1, n_knots)
# Se extiende el vector de nodos agregando multiplicidad 𝑘
# al inicio y al final (necesario para condiciones de contorno en B-splines).
t_uniform = np.concatenate(([0] * k, knots_uniform, [1] * k))

# Base de B-spline con malla inicial
x_data = np.linspace(0, 1, 50)
y_data = f(x_data)
spl_initial = make_lsq_spline(x_data, y_data, t_uniform, k)

# Error local
error_initial = np.abs(spl_initial(x) - y_true)

# Refinamiento adaptativo: insertar más nodos en el centro (donde hay más error)
knots_refined = np.sort(np.concatenate((knots_uniform, [0.45, 0.5, 0.55])))
t_refined = np.concatenate(([0] * k, knots_refined, [1] * k))
spl_refined = make_lsq_spline(x_data, y_data, t_refined, k)

# Error con malla refinada
error_refined = np.abs(spl_refined(x) - y_true)

# ----- Graficar -----
plt.figure(figsize=(10, 5))

# Curvas
plt.subplot(1, 2, 1)
plt.plot(x, y_true, 'k--', label='Función objetivo')
plt.plot(x, spl_initial(x), 'b-', label='B-spline inicial')
plt.plot(x, spl_refined(x), 'r-', label='B-spline refinada')
plt.legend()
plt.title('Aproximación con B-splines')
plt.xlabel('x')
plt.ylabel('y')

# Errores
plt.subplot(1, 2, 2)
plt.plot(x, error_initial, 'b--', label='Error inicial')
plt.plot(x, error_refined, 'r-', label='Error refinado')
plt.legend()
plt.title('Error de aproximación')
plt.xlabel('x')
plt.ylabel('Error')

plt.tight_layout()
plt.savefig('b-spline-example.png', dpi=300)
plt.show()
