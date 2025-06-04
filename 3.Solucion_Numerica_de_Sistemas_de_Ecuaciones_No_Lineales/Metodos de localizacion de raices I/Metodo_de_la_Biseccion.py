'''
METODO DE LA BISECCION

▶ Metodo numerico para encontrar raices de funciones continuas.
▶ Basado en el Teorema del Valor Intermedio.
▶ Se aplica en intervalos donde f (a)f (b) < 0. 

Pasos del Metodo
1. Verificar que f(a)f(b) < 0.
2. Calcular el punto medio: c = (a+b)/2
3. Evaluar f (c):
   Si f(c) = 0, entonces c es la raiz.
   Si f(a)f(c) < 0, actualizar b = c.
   Si f(c)f(b) < 0, actualizar a = c.
4. Repetir hasta que |b - a| < ε.

Ventajas
▶ Convergencia garantizada.
▶ Sencillez del metodo.
Desventajas
▶ Convergencia lenta.
▶ Requiere que f(a)f(b) < 0.
'''
def f(x):
    e=2.71828
    return e**x -(0.1+x**2)**-1
    #return x**3 - x**2 - x - 2

def biseccion(a, b, tol=1e-3, max_iter=100):
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
raiz_aprox = biseccion(0, 1)
print(f"\nAproximación de la raíz: {raiz_aprox}")
