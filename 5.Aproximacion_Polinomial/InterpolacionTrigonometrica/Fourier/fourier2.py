import numpy as np
import matplotlib.pyplot as plt

# Función para evaluar el polinomio trigonométrico interpolante usando coeficientes FFT
def evaluar_interpolante_fft(coeffs, x, L=2):
    """
    Evalúa el polinomio trigonométrico interpolante en puntos x.

    coeffs : array complejo
        Coeficientes FFT normalizados de la función en nodos.
    x : array o float
        Puntos donde evaluar el polinomio.
    L : float
        Longitud del intervalo de interpolación (por defecto 2).
    """
    N = len(coeffs)
    x = np.atleast_1d(x)

    # Se define el polinomio trigonométrico:
    # P(x) = sum_{k=0}^{N-1} coeffs[k] * exp(i * 2*pi * k * x / L)
    # Nota: Usamos la convención de FFT para interpolación periódica en [0, L]
    P_x = np.zeros_like(x, dtype=complex)
    for k in range(N):
        P_x += coeffs[k] * np.exp(1j * 2 * np.pi * k * x / L)
    return np.real(P_x)  # Parte real, porque la función original es real

# --- Código principal ---

# Definir función f(x)
def f(x):
    return x**4 - 3*x**3 + 2*x**2 - np.tan(x*(x-2))

# Nodos equiespaciados en [0,2]
x_nodes = np.linspace(0, 2, 8, endpoint=False)  # 8 nodos (j/4 para j=0..7)
f_nodes = f(x_nodes)

# Calcular coeficientes FFT normalizados
F_coeffs = np.fft.fft(f_nodes) / len(f_nodes)

# Evaluar el polinomio en una malla fina para graficar
x_fine = np.linspace(0, 2, 400)
P_vals = evaluar_interpolante_fft(F_coeffs, x_fine, L=2)

# Graficar función original y polinomio interpolante
plt.figure(figsize=(8,5))
plt.plot(x_fine, f(x_fine), label='Función original $f(x)$', linewidth=2)
plt.plot(x_fine, P_vals, label='Interpolante trigonométrico', linestyle='--')
plt.scatter(x_nodes, f_nodes, color='red', label='Nodos')
plt.title('Interpolación trigonométrica usando FFT')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid(True)
plt.show()
