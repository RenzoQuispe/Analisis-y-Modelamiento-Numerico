import matplotlib.pyplot as plt

def f(x):
    return x**3 - x**2 - x - 2

def regla_falsa(f, a, b, tol=1e-1, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")

    iteraciones = []
    for i in range(max_iter):
        # Cálculo de la nueva aproximación usando la fórmula de la regla falsa
        x = b - f(b) * (b - a) / (f(b) - f(a))
        iteraciones.append((i, x, f(x)))

        # Verificación de la condición de convergencia
        if abs(f(x)) < tol:
            break
        
        # Actualización de los límites de búsqueda
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

    return x, iteraciones

# Ejemplo de uso
raiz, datos = regla_falsa(f, 0.4, 2.5)

# Mostrar resultados
for i, x, fx in datos:
    print(f"Iteración {i + 1}: x = {x:.10f}, f(x) = {fx:.2e}")

# Gráfica de la convergencia
x_vals = [x for _, x, _ in datos]
fx_vals = [fx for _, _, fx in datos]
plt.plot(x_vals, fx_vals, marker='o')
plt.xlabel("Iteraciones")
plt.ylabel("f(x)")
plt.title("Convergencia del Método de Regla Falsa")
plt.grid(True)
plt.show()
