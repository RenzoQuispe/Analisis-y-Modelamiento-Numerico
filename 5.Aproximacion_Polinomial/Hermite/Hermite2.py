import numpy as np
import matplotlib.pyplot as plt

# Nodos y condiciones dadas
x_values = [1, 2]
f_values = [2, 6]
f_prime = [3, 7]
f_double_prime = [8]

# Nodos repetidos para Hermite (para interpolación de Hermite)
z_values = [1, 1, 2, 2, 2]  # Nodo 1 se repite 2 veces, Nodo 2 se repite 3 veces
n = len(z_values)

# Inicializamos la tabla de diferencias divididas (tabla n x n)
Q = np.zeros((n, n))

# Primera columna: valores f(z_i) (función en los puntos dados)
Q[:, 0] = [2, 2, 6, 6, 6]  # f(1), f(1), f(2), f(2), f(2)

# Primera diferencia dividida: asignamos las derivadas y calculamos solo los valores válidos
Q[0, 1] = f_prime[0]  # f'(1)
Q[1, 1] = (Q[2, 0] - Q[1, 0]) / (z_values[2] - z_values[1])  # Normal diferencia dividida
Q[2, 1] = f_prime[1]  # f'(2)
Q[3, 1] = f_prime[1]  # f'(2)

# Segunda columna: calcular diferencias divididas usando derivadas (sin división por cero)
Q[2, 2] = f_double_prime[0] / 2  # Segunda derivada en x=2
Q[0, 2] = (Q[1, 1] - Q[0, 1]) / (z_values[2] - z_values[0])  # Diferencia dividida para el primer término
Q[1, 2] = (Q[2, 1] - Q[1, 1]) / (z_values[3] - z_values[1])  # Diferencia dividida para el segundo término

# Tercera columna: diferencias divididas entre las segundas diferencias
Q[0, 3] = (Q[1, 2] - Q[0, 2]) / (z_values[3] - z_values[0])  # Calculamos la tercera columna
Q[1, 3] = (Q[2, 2] - Q[1, 2]) / (z_values[4] - z_values[1])

# Cuarta columna: calculamos la última diferencia
Q[0, 4] = (Q[1, 3] - Q[0, 3]) / (z_values[4] - z_values[0])

# Imprimir la tabla de diferencias divididas
print("\nTabla de diferencias divididas:")
print(Q)

# Función para evaluar el polinomio de Hermite
def hermite_polynomial(x, z_values, Q):
    n = len(z_values)
    result = Q[0, 0]
    product_term = 1.0
    for i in range(1, n):
        product_term *= (x - z_values[i - 1])
        result += Q[0, i] * product_term
    return result

# Evaluar el polinomio
x_test = np.linspace(1, 2, 100)
y_test = [hermite_polynomial(x, z_values, Q) for x in x_test]

# Graficamos el polinomio y los puntos dados
plt.plot(x_test, y_test, label="Polinomio de Hermite")
plt.scatter(x_values, f_values, color="red", label="Puntos dados")
plt.title("Interpolación de Hermite")
plt.xlabel("x")
plt.ylabel("H(x)")
plt.legend()
plt.grid(True)
plt.show()
