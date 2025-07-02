import numpy as np
import matplotlib.pyplot as plt

def spline_cubico_natural(x, y):
    n = len(x) - 1  # número de intervalos
    h = np.diff(x)
    a = y.copy()

    # Paso 1: Construcción del sistema tridiagonal para c_j
    alpha = h[:-1]
    beta = 2 * (h[:-1] + h[1:])
    gamma = h[1:]
    R = 3 * ((a[2:] - a[1:-1]) / h[1:] - (a[1:-1] - a[:-2]) / h[:-1])

    # Paso 2: Resolver sistema tridiagonal (c_0 y c_n ya se saben = 0)
    c = np.zeros(n + 1)
    # Matriz tridiagonal implícita: alpha, beta, gamma
    # Usamos el algoritmo de Thomas
    c_ = np.zeros(n - 1)
    beta_ = beta.copy()
    R_ = R.copy()

    for i in range(1, n - 1):
        m = alpha[i] / beta_[i - 1]
        beta_[i] = beta_[i] - m * gamma[i - 1]
        R_[i] = R_[i] - m * R_[i - 1]

    c_[n - 2] = R_[n - 2] / beta_[n - 2]
    for i in reversed(range(n - 2)):
        c_[i] = (R_[i] - gamma[i] * c_[i + 1]) / beta_[i]

    c[1:n] = c_

    # Paso 3: Calcular b_j y d_j
    b = np.zeros(n)
    d_coef = np.zeros(n)

    for j in range(n):
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j] / 3 * (2 * c[j] + c[j + 1])
        d_coef[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Paso 4: Devolver funciones por intervalo
    def spline_eval(x_eval):
        x_eval = np.asarray(x_eval)
        s = np.zeros_like(x_eval)
        for j in range(n):
            idx = (x_eval >= x[j]) & (x_eval <= x[j + 1])
            dx = x_eval[idx] - x[j]
            s[idx] = a[j] + b[j]*dx + c[j]*dx**2 + d_coef[j]*dx**3
        return s

    return spline_eval, (a[:-1], b, c[:-1], d_coef)

# === Prueba con los datos del ejemplo ===
x = np.array([1, 2, 3])
y = np.array([2, 3, 5])

spline_func, coef = spline_cubico_natural(x, y)

# Evaluamos en puntos finos
x_fino = np.linspace(1, 3, 200)
y_fino = spline_func(x_fino)

# Graficar
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'ro', label='Puntos dados')
plt.plot(x_fino, y_fino, 'b-', label='Spline cúbico natural')
plt.title('Spline Cúbico Natural (Implementación Propia)')
plt.xlabel('x')
plt.ylabel('S(x)')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar coeficientes por intervalo
a_, b_, c_, d_ = coef
for j in range(len(b_)):
    print(f"Intervalo [{x[j]}, {x[j+1]}]:")
    print(f"  S_{j}(x) = {a_[j]:.4f} + {b_[j]:.4f}(x - {x[j]}) + {c_[j]:.4f}(x - {x[j]})^2 + {d_[j]:.4f}(x - {x[j]})^3")
