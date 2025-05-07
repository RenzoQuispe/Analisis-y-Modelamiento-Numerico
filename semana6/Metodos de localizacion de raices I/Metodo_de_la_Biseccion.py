def f(x):
    return x**3 - x**2 - x - 2

def biseccion(a, b, tol=1e-1, max_iter=100):
    if f(a) * f(b) >= 0:
        print("La función no cumple con f(a) * f(b) < 0.")
        return None

    print(f"{'Iter':>4} | {'a':>10} | {'b':>10} | {'c':>10} | {'f(c)':>12} | {'Error':>10}")
    print("-" * 65)

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        error = abs(b - a) / 2

        print(f"{i:4d} | {a:10.3f} | {b:10.3f} | {c:10.3f} | {fc:12.3e} | {error:10.3e}")

        if abs(fc) < tol or error < tol:
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("Se alcanzó el número máximo de iteraciones.")
    return c

# Ejemplo de uso
raiz_aprox = biseccion(0.4, 2.5)
print(f"\nAproximación de la raíz: {raiz_aprox}")
