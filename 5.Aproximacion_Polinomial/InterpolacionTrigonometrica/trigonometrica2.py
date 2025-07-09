import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Grado
n = 2
N = 2 * n + 1  # Número de nodos

# Nodos theta_k
theta = 2 * np.pi * np.arange(N) / N

# Función exponencial a interpolar
f = lambda theta: np.exp(theta)
f_theta = f(theta)

# Puntos complejos z_k
z_k = np.exp(1j * theta)
y_k = z_k * f_theta  # Transformación compleja

# Interpolación polinomial compleja: Q(z) de grado 4
Q_coeffs = np.polyfit(z_k, y_k, deg=2*n)  # Mayor a menor grado

# Mostrar coeficientes del polinomio Q(z)
print("Coeficientes de Q_4(z):")
for i, c in enumerate(Q_coeffs):
    print(f"  z^{2*n - i} term: {c:.4f}")

# Evaluación en una malla
theta_plot = np.linspace(0, 2*np.pi, 400)
z_plot = np.exp(1j * theta_plot)

# Q(z) y reconstrucción de p_2(θ)
Q_vals = np.polyval(Q_coeffs, z_plot)
p_vals = np.real(np.exp(-1j * theta_plot) * Q_vals)

# Imprimir expresión explícita de p_2(θ)
# Coeficientes de Q(z): [q4, q3, q2, q1, q0] → Q(z) = q4*z^4 + q3*z^3 + q2*z^2 + q1*z + q0
q4, q3, q2, q1, q0 = Q_coeffs

# p(θ) = e^{-iθ}(q4 e^{4iθ} + q3 e^{3iθ} + q2 e^{2iθ} + q1 e^{iθ} + q0)
# → c_2 = q4, c_1 = q3, c_0 = q2, c_{-1} = q1, c_{-2} = q0

c2 = q4
c1 = q3
c0 = q2
c_1 = q1
c_2 = q0

a0 = c0.real
a1 = (c1 + c_1).real
a2 = (c2 + c_2).real
b1 = -1j * (c1 - c_1)
b1 = b1.real
b2 = -1j * (c2 - c_2)
b2 = b2.real

print("\nCoeficientes reales del polinomio trigonométrico p_2(θ):")
print(f"  a_0 = {a0:.4f}")
print(f"  a_1 = {a1:.4f}")
print(f"  a_2 = {a2:.4f}")
print(f"  b_1 = {b1:.4f}")
print(f"  b_2 = {b2:.4f}")

# Función exacta (expresión exponencial)
f_exact = f(theta_plot)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(theta_plot, f_exact, label=r"$f(\theta) = e^{\theta}$", linestyle='--')
plt.plot(theta_plot, p_vals, label=r"$p_2(\theta)$ interpolado", color='red')
plt.scatter(theta, f_theta, color='black', label="Nodos", zorder=5)
plt.xlabel(r"$\theta$")
plt.ylabel(r"$f(\theta)$ / $p_2(\theta)$")
plt.title("Interpolación trigonométrica compleja (n=2) para $f(\\theta) = e^{\\theta}$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
