import numpy as np  
import matplotlib.pyplot as plt

# Datos del problema
x0 = 1
x1 = 2
f_x0 = 2     # p(1)
f_x0_der = 4 # p'(1)
f_x1 = 3     # p(2)

# Paso 1: construir nodos con repetición
x_nodes = np.array([x0, x0, x1])
f_nodes = np.array([f_x0, f_x0, f_x1])

# Paso 2: tabla de diferencias divididas
n = len(x_nodes)
dd_table = np.zeros((n, n))
dd_table[:, 0] = f_nodes

# Primera columna de diferencias divididas
dd_table[1, 1] = f_x0_der  # derivada en x0
dd_table[2, 1] = (dd_table[2, 0] - dd_table[1, 0]) / (x_nodes[2] - x_nodes[1])

# Segunda columna
dd_table[2, 2] = (dd_table[2, 1] - dd_table[1, 1]) / (x_nodes[2] - x_nodes[0])

# Coeficientes del polinomio en forma de Newton
a0 = dd_table[0, 0]
a1 = dd_table[1, 1]
a2 = dd_table[2, 2]

# Función evaluadora del polinomio
def p(x):
    return a0 + a1*(x - x0) + a2*(x - x0)*(x - x0)

# Graficar
x_vals = np.linspace(0.5, 2.5, 400)
y_vals = p(x_vals)

plt.figure(figsize=(8,5))
plt.plot(x_vals, y_vals, label='Polinomio de Hermite', color='blue')
plt.scatter([x0, x1], [f_x0, f_x1], color='red', zorder=5, label='Datos')
plt.title('Interpolación de Hermite (Newton, sin simbólicos)')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Imprimir tabla de diferencias divididas
print("\nTabla de diferencias divididas:")
print(f"{'i':<3} {'x_i':<5} {'f[x_i]':<10} {'f[x_i,x_{i+1}]':<20} {'f[x_i,x_{i+1},x_{i+2}]':<25}")
for i in range(n):
    x_val = x_nodes[i]
    f0 = f"{dd_table[i,0]:.6f}"
    f1 = f"{dd_table[i,1]:.6f}" if i >= 1 else ""
    f2 = f"{dd_table[i,2]:.6f}" if i >= 2 else ""
    print(f"{i:<3} {x_val:<5.1f} {f0:<10} {f1:<20} {f2:<25}")

# Mostrar coeficientes
print(f'Coeficientes de Newton: a0 = {a0}, a1 = {a1}, a2 = {a2}')