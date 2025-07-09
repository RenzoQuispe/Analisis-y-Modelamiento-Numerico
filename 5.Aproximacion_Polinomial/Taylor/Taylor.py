import numpy as np
import matplotlib.pyplot as plt

# Función original y su polinomio de Taylor
def f(x):
    return np.sin(x)

def P3(x):
    return x - (x**3)/6

# Resto estimado con cota de Lagrange: |f⁽⁴⁾(ξ)| ≤ sin(π/4) ≈ 0.707
def error_cota(x):
    M = np.sin(np.pi / 4)  # Máximo valor de |sin(x)| en [-π/4, π/4]
    return (M / 24) * np.abs(x)**4

# Rango de evaluación
#x = np.linspace(-np.pi/4, np.pi/4, 500)
x = np.linspace(-2, 2, 500)

# Calcular valores
f_x = f(x)
p3_x = P3(x)
error_real = np.abs(f_x - p3_x)
error_est = error_cota(x)

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, f_x, label=r'$\sin(x)$', linewidth=2)
plt.plot(x, p3_x, label=r'Polinomio de Taylor $P_3(x)$', linestyle='--')
plt.fill_between(x, p3_x - error_est, p3_x + error_est, color='gray', alpha=0.3, label='Cota de error (Lagrange)')
plt.plot(x, error_real, label='Error real', color='red', linestyle=':')
plt.title('Aproximación de $\\sin(x)$ con Polinomio de Taylor de orden 3')
plt.xlabel('x')
plt.ylabel('Valor')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
