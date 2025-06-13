import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

# Función continua
f = lambda x: np.abs(x - 0.5)

# Polinomios de Bernstein
def bernstein_approx(f, n, x):
    return sum(f(k/n) * comb(n, k) * x**k * (1 - x)**(n - k) for k in range(n+1))

# Dominio
x = np.linspace(0, 1, 400)
y_true = f(x)

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, y_true, label=r'$f(x) = |x - 0.5|$', linewidth=2, color='black')

# Aproximaciones con distintos n
for n, color in zip([5, 10, 20], ['red', 'green', 'blue']):
    y_bernstein = bernstein_approx(f, n, x)
    plt.plot(x, y_bernstein, label=fr'$B_{{{n}}}(x)$', linestyle='--', color=color)

plt.title('Aproximación de $f(x)$ con Polinomios de Bernstein')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('aproximacion_bernstein.png', dpi=300)
plt.show()