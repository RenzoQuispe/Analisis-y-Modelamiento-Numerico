'''
METODO DEL PUNTO FIJO

Queremos resolver la ecuacion:
x = g(x)
Metodo del punto fijo:
1. Reescribimos una ecuacion f(x) = 0 como x = g(x).
2. Definimos la iteracion: xn+1 = g(xn).

Criterio de Convergencia: 
garantizada si:
g(x) continua en [a,b]
g(x) ∈ [a,b] para todo x ∈ [a,b]
|g'(x)| ≤ k < 1 en [a,b]

Conclusiones:
▶ Si |g'(x)| < 1 en un entorno de x*, entonces la iteracion:
xn+1 = g(xn)
converge localmente a x*.
▶ La convergencia es al menos lineal.
▶ Este resultado es una consecuencia directa del Teorema del Punto Fijo de Banach.
'''
import numpy as np
import matplotlib.pyplot as plt

# Definimos g(x) tal que x = g(x) tenga una solución
def g(x):
    return (x**2 + 2) / 3  # raíz de x^2 - 3x + 2 = 0

def punto_fijo(g, x0, tol=1e-2, max_iter=50):
    errores = []
    iteraciones = [x0]

    for i in range(max_iter):
        x1 = g(x0)
        error = abs(x1 - x0)
        errores.append(error)
        iteraciones.append(x1)
        
        print(f"Iteración {i + 1}: x = {x1:.6f}, error = {error:.2e}")
        
        if error < tol:
            break
        
        x0 = x1
    
    return iteraciones, errores

# Ejecutar el método
x0 = 0.8
xs, errs = punto_fijo(g, x0)

# Graficar convergencia del error
plt.figure(figsize=(8, 5))
plt.plot(errs, marker='o')
plt.yscale('log')
plt.title('Convergencia del método del punto fijo')
plt.xlabel('Iteración')
plt.ylabel('Error absoluto (escala logarítmica)')
plt.grid(True)
plt.tight_layout()
plt.show()
