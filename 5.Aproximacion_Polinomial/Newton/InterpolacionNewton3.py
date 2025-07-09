import numpy as np
import matplotlib.pyplot as plt

# Función original (puedes cambiarla)
def funcion_original(x):
    return np.sin(x)  # por ejemplo, seno

# Puntos para interpolar
x_points = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4])
y_points = funcion_original(x_points)

# Cálculo de coeficientes con diferencias divididas
def diferencias_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

# Evaluar polinomio de Newton en x
def polinomio_newton(coef, x_data, x):
    n = len(coef) - 1
    resultado = coef[n]
    for k in range(n - 1, -1, -1):
        resultado = resultado * (x - x_data[k]) + coef[k]
    return resultado

# Obtener coeficientes para puntos dados
coeficientes = diferencias_divididas(x_points, y_points)

# Evaluar en un rango para graficar
x_eval = np.linspace(-1, 3.4, 100)
y_eval = [polinomio_newton(coeficientes, x_points, xi) for xi in x_eval]

# Graficar función original y polinomio interpolante
plt.plot(x_eval, funcion_original(x_eval), label='Función original (sin(x))', color='blue')
plt.plot(x_eval, y_eval, label='Polinomio de Newton', linestyle='--', color='red')
plt.scatter(x_points, y_points, color='black', label='Puntos de interpolación')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación con Polinomio de Newton')
plt.grid(True)
plt.show()
