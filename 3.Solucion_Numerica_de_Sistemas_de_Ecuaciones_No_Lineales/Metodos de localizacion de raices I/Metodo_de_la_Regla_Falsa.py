'''
METODO DE LA REGLA FALSA

▶ El metodo de la regla falsa busca aproximar raices de funciones no lineales.
▶ Tambien se conoce como metodo de la falsa posicion.
▶ Requiere una funcion continua f (x) y un intervalo [a, b] tal
que f(a)f(b) < 0.
Idea del Metodo:
▶ Usa una interpolacion lineal entre los puntos (a, f(a)) y (b, f(b)).
▶ Calcula la raiz de la recta secante:
xr = (b-f(b)(a-b))/(f(a)-f(b))
▶ Se actualiza el intervalo conservando el cambio de signo.

Algoritmo:
1. Elegir a, b tales que f(a)f(b) < 0.
2. Calcular xr usando la formula.
3. Si f (xr) = 0, se encontro la raiz.
4. Si f(a)f(xr) < 0, asignar b = xr ;
   Si f(b)f(xr) < 0, asignar a = xr .
5. Repetir hasta que |f(xr)| < ε.

Comparacion con Otros Metodos
▶ Biseccion: mas lento pero siempre reduce el intervalo a la mitad.
▶ Regla falsa: mas rapida al principio, pero puede estancarse.
▶ Secante y Newton: mas rapidos, pero requieren mas condiciones (derivadas o doble evaluacion).

Conclusion
▶ La regla falsa es un metodo confiable y facil de implementar.
▶ Util cuando se desea una convergencia mas rapida que la biseccion sin necesidad de derivadas.
▶ El metodo de la regla falsa garantiza convergencia si f es continua y cambia de signo.
▶ No siempre es eficiente: puede haber estancamiento.
▶ En esos casos, metodos como la biseccion o la secante pueden ser preferibles.
'''
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
