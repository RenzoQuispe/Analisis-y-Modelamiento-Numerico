import numpy as np
"""
Metodo de Bairstow (Metodo polinomial)
    El método de Bairstow es un algoritmo numérico utilizado para encontrar las raíces (reales o complejas) de polinomios con coeficientes reales,
    y está especialmente diseñado para encontrar raíces complejas conjugadas sin necesidad de recurrir a la aritmética compleja directamente.
    El método de Bairstow sirve para:
    - Encontrar todas las raíces de un polinomio de grado mayor a 2.
    - Resolver polinomios reales sin necesidad de convertir a números complejos.
    - Hallar raíces cuadráticas (es decir, se basa en dividir el polinomio en factores de segundo grado).
    Es particularmente útil cuando:
    - Se tienen polinomios de grado alto.
    - Se desea automatizar el proceso (por ejemplo, en calculadoras o software).
"""
def bairstow_method(a, u, v, tol=1e-6, max_iter=100):
    n = len(a) - 1
    roots = []

    while n >= 3:
        b = np.zeros(n + 1)
        c = np.zeros(n + 1)
        b[n] = a[n]
        c[n] = 0
        c[n - 1] = a[n]

        for j in range(1, max_iter + 1):
            b[n - 1] = a[n - 1] + u * b[n]
            for k in range(n - 2, -1, -1):
                b[k] = a[k] + u * b[k + 1] + v * b[k + 2]
                c[k] = b[k + 1] + u * c[k + 1] + v * c[k + 2]

            J = c[0] * c[2] - c[1]**2
            if abs(J) < 1e-14:
                print("Jacobiano casi nulo. Deteniendo iteración.")
                break

            du = (c[1] * b[1] - c[2] * b[0]) / J
            dv = (c[1] * b[0] - c[0] * b[1]) / J

            u = u + du
            v = v + dv

            print(f"Iteración {j}: u = {u:.8f}, v = {v:.8f}, b[0] = {b[0]:.8f}, b[1] = {b[1]:.8f}")

            if abs(du) < tol and abs(dv) < tol:
                break

        # Calcular raíces del factor cuadrático x^2 + ux + v
        D = u ** 2 - 4 * v
        if D >= 0:
            r1 = (-u + np.sqrt(D)) / 2
            r2 = (-u - np.sqrt(D)) / 2
        else:
            r1 = complex(-u / 2, np.sqrt(-D) / 2)
            r2 = complex(-u / 2, -np.sqrt(-D) / 2)

        roots.extend([r1, r2])

        # División sintética para reducir el polinomio
        a = b[2:n + 1]
        n = len(a) - 1

    # Resolver el resto (grado 2 o 1)
    if n == 2:
        a2, a1, a0 = a[2], a[1], a[0]
        D = a1 ** 2 - 4 * a2 * a0
        if D >= 0:
            r1 = (-a1 + np.sqrt(D)) / (2 * a2)
            r2 = (-a1 - np.sqrt(D)) / (2 * a2)
        else:
            r1 = complex(-a1 / (2 * a2), np.sqrt(-D) / (2 * a2))
            r2 = complex(-a1 / (2 * a2), -np.sqrt(-D) / (2 * a2))
        roots.extend([r1, r2])
    elif n == 1:
        roots.append(-a[0] / a[1])

    return roots

# Polinomio p(z) = z^4 - 4z^3 + 7z^2 - 5z - 2
a = np.array([-2, -5, 7, -4, 1][::-1], dtype=float)

# Estimaciones iniciales
u = 3.0
v = -4.0

# Ejecutar método de Bairstow
raices = bairstow_method(a, u, v)

# Mostrar raíces
print("\nRaíces encontradas:")
for r in raices:
    print(r)