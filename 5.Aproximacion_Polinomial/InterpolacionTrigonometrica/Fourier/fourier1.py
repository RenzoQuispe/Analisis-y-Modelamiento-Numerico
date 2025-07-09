import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x)
def f(x):
    return x**4 - 3*x**3 + 2*x**2 - np.tan(x*(x-2))

# Nodos dados en [0,2]
x_nodes = np.array([j/4 for j in range(8)])  # j=0,...,7
f_nodes = f(x_nodes)

# Cambio de variable z = pi * x para aplicar FFT en nodos z_j = j*pi/4
z_nodes = np.pi * x_nodes
f_z_nodes = f_nodes  # f(z_j/pi) = f(x_j)

# --- Parte 1: Ejemplo simple con 4 datos (los primeros 4 puntos) ---
x_small = np.array([0, np.pi/2, np.pi, 3*np.pi/2])
f_small = f(x_small/np.pi*2)  # reescalamos para aproximar f(x) en [0,2]

# Coeficientes alpha y beta
alpha_0 = 0.5 * (f_small[0] + f_small[2])
alpha_1 = 0.5 * (f_small[0] - f_small[2])
beta_0 = 0.5 * (f_small[1] + f_small[3])
beta_1 = 0.5 * (f_small[1] - f_small[3])

# Coeficientes gamma
gamma_0 = 0.5 * (alpha_0 + beta_0)
gamma_1 = 0.5 * (alpha_1 - 1j * beta_1)
gamma_2 = 0.5 * (alpha_0 - beta_0)
gamma_3 = 0.5 * (alpha_1 + 1j * beta_1)

gamma = np.array([gamma_0, gamma_1, gamma_2, gamma_3])

# Función base E_j(x) = e^{i j x}, j=0..3
def E(j, x):
    return np.exp(1j * j * x)

# Construir P(x)
def P(x):
    return sum(gamma[j] * E(j, x) for j in range(4))

# Evaluar P(x) en un rango para graficar
x_plot = np.linspace(0, 3*np.pi/2, 400)
P_vals = np.real([P(xi) for xi in x_plot])

plt.figure(figsize=(8,4))
plt.plot(x_plot, P_vals, label='Interpolante $P(x)$')
plt.scatter(x_small, f_small, color='red', label='Datos')
plt.title('Interpolación trigonométrica (Ejemplo con 4 puntos)')
plt.xlabel('$x$')
plt.ylabel('$P(x)$')
plt.legend()
plt.grid(True)
plt.show()

# --- Parte 2: FFT para los 8 nodos y polinomio de grado 4 en [0,2] ---

# Aplicar FFT a f(z_j/pi)
F_coeffs = np.fft.fft(f_z_nodes) / len(f_z_nodes)  # Normalizamos

# Mostrar coeficientes relevantes para polinomio grado 4 (frecuencias 0 a 4)
print("Coeficientes FFT (complejos):")
for k in range(5):
    print(f"A_{k} = {F_coeffs[k]}")

# Puedes usar estos coeficientes para reconstruir/interpolar f en [0,2]
