import numpy as np
import matplotlib.pyplot as plt

# Función original
def f(x): return np.log(x + 1)

# Paso 1: Nodos y valores
x = np.array([0.0, 1.0, 2.0])
y = f(x)

# Paso 2: h_j
h = np.diff(x)
a = y.copy()
n = len(x) - 1

# Paso 3: Calcular c_j (sólo c1, c0 y c2 = 0 por condiciones naturales)
c = np.zeros(n + 1)
rhs = 3 * ((a[2] - a[1]) / h[1] - (a[1] - a[0]) / h[0])
c[1] = rhs / (2 * (h[0] + h[1]))

# Paso 4: Calcular b_j y d_j
b = np.zeros(n)
d_coef = np.zeros(n)

for j in range(n):
    b[j] = (a[j + 1] - a[j]) / h[j] - h[j] / 3 * (2 * c[j] + c[j + 1])
    d_coef[j] = (c[j + 1] - c[j]) / (3 * h[j])

# Paso 5: Función de evaluación del spline
def spline_eval(x_eval):
    x_eval = np.asarray(x_eval)
    s = np.zeros_like(x_eval)
    for j in range(n):
        idx = (x_eval >= x[j]) & (x_eval <= x[j + 1])
        dx = x_eval[idx] - x[j]
        s[idx] = a[j] + b[j]*dx + c[j]*dx**2 + d_coef[j]*dx**3
    return s

# Evaluar y graficar
x_fino = np.linspace(0, 2, 200)
y_fino = spline_eval(x_fino)

plt.figure(figsize=(8, 5))
plt.plot(x_fino, f(x_fino), 'g--', label='f(x) = ln(x+1)')
plt.plot(x_fino, y_fino, 'b-', label='Spline cúbico natural')
plt.plot(x, y, 'ro', label='Nodos')
plt.title('Spline cúbico natural vs f(x) = ln(x+1)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Guardar la figura como imagen PNG
plt.savefig("spline_ln_graph.png", dpi=300, bbox_inches='tight')
plt.show()