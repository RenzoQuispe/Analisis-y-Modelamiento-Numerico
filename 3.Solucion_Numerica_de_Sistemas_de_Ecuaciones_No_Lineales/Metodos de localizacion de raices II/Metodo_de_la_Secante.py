'''
METODO DE LA SECANTE

▶ Metodo numerico para encontrar raices de una funcion f(x) = 0.
▶ Utiliza dos aproximaciones iniciales x0 y x1.
▶ Sustituye la derivada en Newton-Raphson por una pendiente secante.

Algoritmo
1. Elige x0 y x1 cercanos a la raiz.
2. Calcula xn+1 usando la formula iterativa.
3. Verifica si |f(xn+1)| < ε.
4. Si no se cumple, actualizar: xn-1 <- xn , xn <- xn+1 y repetir

Ventajas:
▶ No requiere derivada.
▶ Convergencia superlineal.
▶ Mas rapido que biseccion o regla falsa.
Desventajas:
▶ No garantiza convergencia.
▶ Sensible a malas aproximaciones iniciales

Comparaciones:
Criterio                  |        Regla Falsa        |      Secante
Cambio de signo requerido |             Si            |       No
Puntos iniciales          |  a, b con f (a)f (b) < 0  | x0, x1 arbitrarios
Intervalo garantiza raiz  |            Si             | No necesariamente
-----------------------------------------------------------------------------
Criterio              | Regla Falsa |    Secante
Tipo de convergencia  |   Lineal    |  Superlineal
Robustez              |    Alta     |     Menor
Estancamiento posible |     Si      |  Menos probable
Velocidad general     | Mas lenta   |   Mas rapida
-----------------------------------------------------------------------------
Regla Falsa:
+ Siempre encierra la raiz.
+ Convergencia segura si f es continua y cambia de signo.
- Puede estancarse si un extremo no se actualiza.
Secante:
+ Mas rapida que la regla falsa y biseccion.
- No garantiza encerrar la raiz.
- Puede diverger si los puntos iniciales no son buenos.
------------------------------------------------------------------------------
Metodo         | Derivada |Intervalo con signo|  Velocidad
Biseccion      |    No    |        Si         | Lenta (lineal)
Regla Falsa    |    No    |        Si         | Lenta (mejor que biseccion)
Secante        |    No    |        No         | Rapida (superlineal)
Newton-Raphson |    Si    |        No         | Muy rapida (cuadratica)


Conclusiones:
▶ El metodo de la secante es eficiente y facil de implementar.
▶ Ideal cuando no se dispone de derivadas.
▶ Requiere buenas estimaciones iniciales para garantizar el exito.
▶ Regla Falsa: buena eleccion cuando se desea robustez.
▶ Secante: util cuando se busca rapidez y se tiene una buena estimacion inicial.
▶ Ambos son utiles dependiendo del contexto y naturaleza de la funcion.
▶ El metodo de la secante no garantiza convergencia si:
▶ La derivada es cero o infinita cerca de la raiz.
▶ La funcion tiene raices multiples.
▶ En este caso, la falta de derivada en x = 0 provoca que el metodo falle.
'''

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x**2 - x - 2

# Método de la secante
def secante(f, x0, x1, tol=1e-2, max_iter=6):
    xs = [x0, x1]
    for i in range(max_iter):
        f0, f1 = f(x0), f(x1)
        if f1 - f0 == 0:
            print("División por cero.")
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        xs.append(x2)
        print(f"Iteración {i+1}: x = {x2:.6f}, f(x) = {f(x2):.6f}")
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2
    return xs

# Ejecutar el método
x0, x1 = 0.4, 2.5
iteraciones = secante(f, x0, x1)

# Crear la gráfica
x = np.linspace(x0 - 0.5, x1 + 0.5, 500)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = x^3 - x^2 - x - 2$', color='blue')
plt.axhline(0, color='gray', linewidth=0.5)

# Marcar puntos y etiquetar
for i, xi in enumerate(iteraciones):
    yi = f(xi)
    plt.plot(xi, yi, 'ko')
    plt.text(xi + 0.05, yi - 0.3, f'$x_{{{i}}}$', fontsize=10)

plt.legend()
plt.title("Método de la Secante")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
