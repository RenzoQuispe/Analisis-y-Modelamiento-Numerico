import numpy as np
import math
import matplotlib.pyplot as plt

# Construye tabla de diferencias regresivas
def diferencias_regresivas(y):
    n = len(y)
    tabla = np.zeros((n, n))
    tabla[:, 0] = y
    for j in range(1, n):
        for i in range(j, n):
            tabla[i, j] = tabla[i, j-1] - tabla[i-1, j-1]
    return tabla

# Coeficiente binomial generalizado: (s choose k)
def coef_binomial(s, k):
    resultado = 1
    for i in range(k):
        resultado *= (s + i)
    return resultado / math.factorial(k)

# Evaluar polinomio de Newton regresivo
def newton_regresivo(x_nodes, y_nodes, x_eval):
    h = x_nodes[1] - x_nodes[0]
    tabla = diferencias_regresivas(y_nodes)
    n = len(x_nodes)
    s = (x_eval - x_nodes[-1]) / h  # regresivo: desde último nodo
    resultado = tabla[n - 1, 0]
    for k in range(1, n):
        resultado += coef_binomial(s, k) * tabla[n - 1, k]
    return resultado

# === EJEMPLO ===

# Datos equidistantes
x_nodes = np.array([0, 1, 2, 3])
y_nodes = x_nodes**2 + x_nodes + 1  # f(x) = x^2 + x + 1

# Evaluar en varios puntos
x_vals = np.linspace(-0.5, 3.5, 200)
y_interp = [newton_regresivo(x_nodes, y_nodes, x) for x in x_vals]
y_real = x_vals**2 + x_vals + 1

# Gráfica
plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_real, label='Función original', color='blue')
plt.plot(x_vals, y_interp, '--', label='Interpolación (Newton regresivo)', color='red')
plt.scatter(x_nodes, y_nodes, color='black', label='Puntos de interpolación')
plt.title("Interpolación con Newton Regresivo")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
