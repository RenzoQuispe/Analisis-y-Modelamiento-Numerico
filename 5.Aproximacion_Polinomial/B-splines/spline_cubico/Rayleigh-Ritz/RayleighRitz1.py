import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.linalg import solve

# Número de funciones base
n = 9
h = 1 / (n + 1)

# Nodos
x_nodes = np.linspace(0, 1, n + 2)

# B-spline cúbica básica
def S(x):
    if x < -2 or x > 2:
        return 0.0
    elif -2 <= x < -1:
        return (1/6)*(2 + x)**3
    elif -1 <= x < 0:
        return (1/6)*((2 + x)**3 - 4*(1 + x)**3)
    elif 0 <= x < 1:
        return (1/6)*((2 - x)**3 - 4*(1 - x)**3)
    elif 1 <= x <= 2:
        return (1/6)*(2 - x)**3
    else:
        return 0.0

# Derivada analítica de la B-spline cúbica
def dS(x):
    if -2 <= x < -1:
        return 0.5*(2 + x)**2
    elif -1 <= x < 0:
        return 0.5*((2 + x)**2 - 4*(1 + x)**2)
    elif 0 <= x < 1:
        return -0.5*((2 - x)**2 - 4*(1 - x)**2)
    elif 1 <= x <= 2:
        return -0.5*(2 - x)**2
    else:
        return 0.0

# Funciones base phi_i(x) y su derivada
def phi(i, x):
    return S((x - x_nodes[i]) / h)

def dphi(i, x):
    return (1 / h) * dS((x - x_nodes[i]) / h)

# Funciones del problema
def p(x): return 1
def q(x): return np.pi**2
def f(x): return 2*np.pi**2 * np.sin(np.pi * x)
def y_exact(x): return np.sin(np.pi * x)

# Inicializar matriz A y vector b
A = np.zeros((n, n))
b = np.zeros(n)

# Construcción de A (solo nodos internos)
for i in range(1, n+1):
    for j in range(max(1, i - 3), min(n + 1, i + 4)):
        xL = max(x_nodes[max(i-2, 0)], 0)
        xU = min(x_nodes[min(i+2, n+1)], 1)
        integrand = lambda x: p(x) * dphi(i, x) * dphi(j, x) + q(x) * phi(i, x) * phi(j, x)
        A[i-1, j-1], _ = quad(integrand, xL, xU)
        A[j-1, i-1] = A[i-1, j-1]

# Construcción del vector b
for i in range(1, n+1):
    xL = max(x_nodes[max(i-2, 0)], 0)
    xU = min(x_nodes[min(i+2, n+1)], 1)
    integrand_b = lambda x: f(x) * phi(i, x)
    b[i-1], _ = quad(integrand_b, xL, xU)

# Resolver el sistema
c_internal = solve(A, b)
c = np.zeros(n + 2)
c[1:n+1] = c_internal  # Las condiciones de contorno ya están incorporadas

# Aproximación
x_plot = np.linspace(0, 1, 500)
y_approx = np.zeros_like(x_plot)
for i in range(n + 2):
    y_approx += c[i] * np.array([phi(i, x) for x in x_plot])

# Solución exacta
y_true = y_exact(x_plot)

# Cálculo del error L2: integral de (y_true - y_approx)^2 dx
error_integrand = lambda x: (np.sin(np.pi * x) - sum(c[i]*phi(i, x) for i in range(n+2)))**2
error_L2, _ = quad(error_integrand, 0, 1)

print(f"Error total L2: {error_L2:.6e}")

# Gráfico
plt.figure(figsize=(10, 5))
plt.plot(x_plot, y_true, label='Solución exacta $y(x) = \sin(\pi x)$', color='black', linestyle='--')
plt.plot(x_plot, y_approx, label='Aproximación Rayleigh–Ritz con B-splines', color='blue')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Comparación entre solución exacta y aproximación\nError L2 = {:.2e}'.format(error_L2))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
