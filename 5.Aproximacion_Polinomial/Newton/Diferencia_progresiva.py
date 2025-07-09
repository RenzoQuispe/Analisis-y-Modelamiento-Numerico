import numpy as np
import math
import matplotlib.pyplot as plt

# Función para construir tabla de diferencias progresivas
def diferencias_progresivas(y):
    n = len(y)
    tabla = np.zeros((n, n))
    tabla[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            tabla[i, j] = tabla[i+1, j-1] - tabla[i, j-1]
    return tabla

# Coeficiente binomial generalizado: (s choose k)
def coef_binomial(s, k):
    resultado = 1
    for i in range(k):
        resultado *= (s - i)
    return resultado / math.factorial(k)

# Evaluar el polinomio de Newton progresivo
def newton_progresivo(x_nodes, y_nodes, x_eval):
    h = x_nodes[1] - x_nodes[0]
    tabla = diferencias_progresivas(y_nodes)
    x0 = x_nodes[0]
    s = (x_eval - x0) / h
    resultado = tabla[0, 0]
    for k in range(1, len(x_nodes)):
        term = coef_binomial(s, k) * tabla[0, k]
        resultado += term
    return resultado

# === EJEMPLO ===

# Puntos equidistantes
x_nodes = np.array([0, 1, 2, 3])
y_nodes = x_nodes**2 + x_nodes + 1  # y = x^2 + x + 1

# Evaluar en un rango
x_vals = np.linspace(-0.5, 3.5, 200)
y_interp = [newton_progresivo(x_nodes, y_nodes, x) for x in x_vals]
y_real = x_vals**2 + x_vals + 1  # Para comparar

# Gráfica
plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_real, label="Función original", color="blue")
plt.plot(x_vals, y_interp, '--', label="Interpolación de Newton (progresiva)", color="red")
plt.scatter(x_nodes, y_nodes, color="black", label="Puntos de interpolación")
plt.title("Interpolación con Newton progresivo")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
