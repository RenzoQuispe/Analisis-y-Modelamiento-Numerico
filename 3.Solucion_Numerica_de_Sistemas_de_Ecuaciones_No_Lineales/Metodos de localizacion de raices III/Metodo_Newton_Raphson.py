'''
Metodo iterativo para encontrar raices de funciones no lineales.
'''
import math

def f(x):
    return x**2 - 2

def df(x):
    return 2 * x  # Derivada de la función

def newton_raphson(x0, tol=1e-6, max_iter=100, derivada_fija=False):
    print(f"{'Iter':<5} {'x_n':<15} {'f(x_n)':<15}")
    print("-" * 40)

    if derivada_fija:
        dfx0 = df(x0)

    for i in range(max_iter):
        fx = f(x0)
        if abs(fx) < tol:
            print(f"\nConvergencia alcanzada en {i} iteraciones.")
            return x0

        if derivada_fija:
            dfx = dfx0
        else:
            dfx = df(x0)

        if dfx == 0:
            raise ZeroDivisionError("La derivada es cero. Método fallido.")

        x1 = x0 - fx / dfx
        print(f"{i:<5} {x0:<15.10f} {fx:<15.10f}")
        x0 = x1

    print("\nNo se alcanzó la convergencia en el número máximo de iteraciones.")
    return x0

# Método clásico (derivada recalculada)
raiz = newton_raphson(x0=0.5)

# Método con derivada fija
#raiz_fija = newton_raphson(x0=0.5, derivada_fija=True)
