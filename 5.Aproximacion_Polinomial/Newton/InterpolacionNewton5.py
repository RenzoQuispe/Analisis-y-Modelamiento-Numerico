import numpy as np
import matplotlib.pyplot as plt
import math  # Usado para factorial

# Función original y derivada superior (acotada por 1 para sin(x))
def funcion_original(x):
    return np.sin(x)

# Puntos de interpolación
#x_points = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4])
x_points = np.array([0, np.pi/4, np.pi/2])
y_points = funcion_original(x_points)

# Diferencias divididas
def diferencias_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

# Evaluar el polinomio de Newton en un punto o arreglo de puntos
def polinomio_newton(coef, x_data, x):
    n = len(coef) - 1
    resultado = coef[n]
    for k in range(n - 1, -1, -1):
        resultado = resultado * (x - x_data[k]) + coef[k]
    return resultado

# Cálculo del error teórico
def error_teorico(x, x_nodes, M=1):
    omega = np.ones_like(x)
    for xi in x_nodes:
        omega *= (x - xi)
    return np.abs(M * omega / math.factorial(len(x_nodes)))

# Obtener coeficientes del polinomio de Newton
coef = diferencias_divididas(x_points, y_points)

# Evaluar sobre un rango para graficar
x_eval = np.linspace(-1, 3.4, 400)
y_real = funcion_original(x_eval)
y_interp = [polinomio_newton(coef, x_points, xi) for xi in x_eval]
error_real = np.abs(y_real - y_interp)
error_bound = error_teorico(x_eval, x_points, M=1)  # Máximo valor de |f⁴(x)| para sin(x)

# Mostrar máximo error real y teórico
print(f"Máximo error real:     {np.max(error_real):.6f}")
print(f"Máxima cota teórica:   {np.max(error_bound):.6f}")

# Gráfico 1: función original y polinomio
plt.figure(figsize=(10, 5))
plt.plot(x_eval, y_real, label='Función original (sin(x))', color='blue')
plt.plot(x_eval, y_interp, label='Polinomio de Newton', linestyle='--', color='red')
plt.scatter(x_points, y_points, color='black', label='Puntos de interpolación')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de sin(x) con Polinomio de Newton')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2: error real vs cota teórica
plt.figure(figsize=(10, 4))
plt.plot(x_eval, error_real, label='|f(x) - P(x)| (Error real)', color='purple')
plt.plot(x_eval, error_bound, label='Cota teórica del error', linestyle='--', color='orange')
plt.xlabel('x')
plt.ylabel('Error')
plt.title('Error de Interpolación de sin(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
