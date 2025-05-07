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
