import numpy as np
"""
METODO DE LA POTENCIA ESCALADO
▶ Variante del metodo de la potencia con mejor estabilidad numerica.
▶ En lugar de normalizar con la norma ∥x^(k)∥, se escala con:
µ^(k) = max(i)(|yi^(k)|)
▶ Algoritmo:
1. Calcular y^(k) = Ax^(k)
2. Escalar: x^(k+1) = y^(k)/µ^(k)
3. Aproximar λ^(k) ≈ µ^(k)
▶ Evita errores de redondeo o desbordamientos.
"""
# Matriz A

A = np.array([[-3, 1],     # sus autovalores son 2 y -3
              [0, 2]])

# Vector inicial x0 (debe ser no nulo)
x = np.array([1.0, 1.0])

# Tolerancia y número máximo de iteraciones
tol = 1e-6
max_iter = 100

k = 0
while True:
    k += 1

    # Paso 1: calcular x_hat = A * x
    x_hat = A @ x

    # Paso 2: escalar x_hat dividiendo por el máximo valor absoluto
    mu = np.max(np.abs(x_hat))
    # mu1 =
    x_new = x_hat / mu

    # Condición de parada: cambio pequeño entre iteraciones
    if np.linalg.norm(x_new - x, ord=np.inf) < tol or k >= max_iter:
        break

    # Actualizar x
    x = x_new

    print(f"Iteración {k}: μ ≈ {mu:.6f}, x ≈ {x}")

# Mostrar resultado final
print("\nResultado final:")
print(f"Valor propio dominante aproximado: {mu:.6f}")
print(f"Vector propio aproximado (normalizado): {x_new}")