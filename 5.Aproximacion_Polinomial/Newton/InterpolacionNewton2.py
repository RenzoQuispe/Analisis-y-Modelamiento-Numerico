import numpy as np
import matplotlib.pyplot as plt

def diferencias_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

def polinomio_newton(coef, x_data, x):
    n = len(coef) - 1
    resultado = coef[n]
    for k in range(n - 1, -1, -1):
        resultado = resultado * (x - x_data[k]) + coef[k]
    return resultado

# Puntos dados
x_points = np.array([1, 3, 5, 6])
y_points = np.array([-3, 1, 2, 4])

# Calcular coeficientes
coeficientes = diferencias_divididas(x_points, y_points)
print("Coeficientes del polinomio de Newton:")
print(coeficientes)

# Evaluar el polinomio en un punto específico
x_eval = 4
valor = polinomio_newton(coeficientes, x_points, x_eval)
print(f"Valor del polinomio en x = {x_eval}: {valor}")

# Evaluar en un rango para graficar
x_vals = np.linspace(min(x_points)-1, max(x_points)+1, 200)
y_vals = [polinomio_newton(coeficientes, x_points, xi) for xi in x_vals]

# Graficar
plt.figure(figsize=(8,5))
plt.plot(x_vals, y_vals, label='Polinomio de Newton', color='red')
plt.scatter(x_points, y_points, color='blue', label='Puntos dados')
plt.axvline(x=x_eval, color='gray', linestyle='--', label=f'x = {x_eval}')
plt.scatter([x_eval], [valor], color='green', zorder=5, label=f'P({x_eval}) = {valor:.2f}')
plt.title('Interpolación con el Polinomio de Newton')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
