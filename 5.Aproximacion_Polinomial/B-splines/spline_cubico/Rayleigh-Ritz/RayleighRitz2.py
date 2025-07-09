import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve

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

# Derivada de la B-spline
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

# Coeficientes del problema
def p(x): return 1
def q(x): return np.pi**2
def f(x): return 2 * np.pi**2 * np.sin(np.pi * x)
def y_exact(x): return np.sin(np.pi * x)

# Cálculo del error para un valor de n
def compute_error(n):
    h = 1 / (n + 1)
    x_nodes = np.linspace(0, 1, n + 2)

    def phi(i, x): return S((x - x_nodes[i]) / h)
    def dphi(i, x): return (1 / h) * dS((x - x_nodes[i]) / h)

    A = np.zeros((n, n))
    b = np.zeros(n)

    for i in range(1, n+1):
        for j in range(max(1, i - 3), min(n + 1, i + 4)):
            xL = max(x_nodes[max(i-2, 0)], 0)
            xU = min(x_nodes[min(i+2, n+1)], 1)
            integrand = lambda x: p(x)*dphi(i, x)*dphi(j, x) + q(x)*phi(i, x)*phi(j, x)
            A[i-1, j-1], _ = quad(integrand, xL, xU)
            A[j-1, i-1] = A[i-1, j-1]

    for i in range(1, n+1):
        xL = max(x_nodes[max(i-2, 0)], 0)
        xU = min(x_nodes[min(i+2, n+1)], 1)
        integrand_b = lambda x: f(x) * phi(i, x)
        b[i-1], _ = quad(integrand_b, xL, xU)

    c_internal = solve(A, b)
    c = np.zeros(n + 2)
    c[1:n+1] = c_internal

    # Error L2
    error_integrand = lambda x: (y_exact(x) - sum(c[i]*phi(i, x) for i in range(n+2)))**2
    error_L2_squared, _ = quad(error_integrand, 0, 1)
    error_L2 = np.sqrt(error_L2_squared)

    # Error máximo (L infinito)
    x_fine = np.linspace(0, 1, 1000)
    error_max = max(
        abs(y_exact(x) - sum(c[i]*phi(i, x) for i in range(n+2)))
        for x in x_fine
    )

    return h, error_L2, error_max

# Pruebas para distintos valores de h
hs = [0.1, 0.05, 0.025, 0.0125, 0.00625]
ns = [int(1/h - 1) for h in hs]

errors = []

for n in ns:
    h, error_L2, error_max = compute_error(n)
    errors.append((h, error_L2, error_max))

# Cálculo de órdenes
orders_L2 = []
orders_max = []

for i in range(1, len(errors)):
    h1, e1_L2, e1_max = errors[i-1]
    h2, e2_L2, e2_max = errors[i]

    order_L2 = np.log(e1_L2 / e2_L2) / np.log(h1 / h2)
    order_max = np.log(e1_max / e2_max) / np.log(h1 / h2)

    orders_L2.append(order_L2)
    orders_max.append(order_max)

# Mostrar resultados
print(" h        |   Error L2     | Orden L2 |  Error máx    | Orden máx")
print("--------------------------------------------------------------------")
for i, (h, eL2, emax) in enumerate(errors):
    oL2 = f"{orders_L2[i-1]:.2f}" if i > 0 else "---"
    omax = f"{orders_max[i-1]:.2f}" if i > 0 else "---"
    print(f"{h:.5f}   | {eL2:.3e} | {oL2:>8} | {emax:.3e} | {omax:>9}")
