import numpy as np
import matplotlib.pyplot as plt

# Función original y su derivada
def f(x):
    return np.log(x + 1)

def df(x):
    return 1 / (x + 1)

# Nodos
x = np.array([0, 1, 2], dtype=float)
y = f(x)

h = np.diff(x)

# Matriz A
A = np.array([
    [2*h[0], h[0], 0],
    [h[0], 2*(h[0] + h[1]), h[1]],
    [0, h[1], 2*h[1]]
])

# Vector R
R = np.array([
    3*((y[1] - y[0])/h[0] - df(x[0])),
    3*((y[2] - y[1])/h[1] - (y[1] - y[0])/h[0]),
    3*(df(x[2]) - (y[2] - y[1])/h[1])
])

# Resolver para c
c = np.linalg.solve(A, R)

# Calcular b y d
b = np.zeros(2)
d = np.zeros(2)

b[0] = (y[1] - y[0])/h[0] - h[0]/3 * (2*c[0] + c[1])
b[1] = (y[2] - y[1])/h[1] - h[1]/3 * (2*c[1] + c[2])

d[0] = (c[1] - c[0]) / (3*h[0])
d[1] = (c[2] - c[1]) / (3*h[1])

def spline_eval(x_eval):
    if x_eval < x[0] or x_eval > x[-1]:
        raise ValueError("x fuera del rango de interpolación")
    if x_eval <= x[1]:
        j = 0
    else:
        j = 1
    dx = x_eval - x[j]
    return y[j] + b[j]*dx + c[j]*dx**2 + d[j]*dx**3

# Evaluar y graficar
x_fino = np.linspace(0, 2, 200)
y_fino = np.array([spline_eval(xi) for xi in x_fino])

plt.figure(figsize=(8, 5))
plt.plot(x_fino, f(x_fino), 'g--', label='f(x) = ln(x+1)')
plt.plot(x_fino, y_fino, 'b-', label='Spline cúbico sujeto')
plt.plot(x, y, 'ro', label='Nodos')
plt.title('Spline cúbico sujeto vs f(x) = ln(x+1)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.savefig('spline_cubico_sujeto.png')
plt.show()
