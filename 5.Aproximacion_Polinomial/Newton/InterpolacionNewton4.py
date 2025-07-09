import numpy as np
import matplotlib.pyplot as plt

# Función original
def funcion_original(x):
    return np.sin(x)

# Puntos para interpolar
x_points = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4])
y_points = funcion_original(x_points)

# Diferencias divididas para obtener coeficientes
def diferencias_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

# Evaluar polinomio de Newton
def polinomio_newton(coef, x_data, x):
    n = len(coef) - 1
    resultado = coef[n]
    for k in range(n - 1, -1, -1):
        resultado = resultado * (x - x_data[k]) + coef[k]
    return resultado

# Obtener coeficientes del polinomio
coeficientes = diferencias_divididas(x_points, y_points)

# Evaluación sobre un rango
x_eval = np.linspace(-1, 3.4, 400)
y_real = funcion_original(x_eval)
y_interp = [polinomio_newton(coeficientes, x_points, xi) for xi in x_eval]
error = np.abs(y_real - y_interp)

# Gráfico 1: Función y polinomio
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

# Gráfico 2: Error de interpolación
plt.figure(figsize=(10, 4))
plt.plot(x_eval, error, label='|Error| = |f(x) - P(x)|', color='purple')
plt.xlabel('x')
plt.ylabel('Error absoluto')
plt.title('Error de Interpolación de sin(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
