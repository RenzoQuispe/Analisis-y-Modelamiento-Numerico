'''
El método de Crout adaptado a matrices tridiagonales es muy
eficiente y se usa para resolver sistemas lineales Ax = b donde A es
tridiagonal, es decir, solo tiene elementos distintos de cero en la
diagonal principal y en las diagonales justo arriba y debajo de esta.
▶ Factoriza una matriz A como A = LU
▶ L: triangular inferior (no necesariamente con unos en la
diagonal)
▶ U: triangular superior con unos en la diagonal
▶ Se utiliza especialmente para matrices tridiagonales.
▶ El orden de las operaciones es importante para evaluar la
eficiencia (complejidad).
Conclusiones
▶ El método de Crout es *lineal* O(n) para matrices
tridiagonales.
▶ Evita almacenar la matriz completa
▶ Este enfoque es mucho más eficiente que e enfoque general de
factorización LU, que tiene complejidad O(n3 ).
'''
def crout_tridiagonal(a, b, c, d):
    n = len(b)
    l = [0.0] * n
    u = [0.0] * (n - 1)
    y = [0.0] * n
    x = [0.0] * n

    # Paso 1: Factorización LU
    l[0] = b[0]
    u[0] = c[0] / l[0]

    for i in range(1, n - 1):
        l[i] = b[i] - a[i - 1] * u[i - 1]
        u[i] = c[i] / l[i]
    l[n - 1] = b[n - 1] - a[n - 2] * u[n - 2]

    # Paso 2: Sustitución hacia adelante (Ly = d)
    y[0] = d[0] / l[0]
    for i in range(1, n):
        y[i] = (d[i] - a[i - 1] * y[i - 1]) / l[i]

    # Paso 3: Sustitución hacia atrás (Ux = y)
    x[n - 1] = y[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = y[i] - u[i] * x[i + 1]

    return x

# --- Ejemplo del sistema ---
a = [2, 3]         # Subdiagonal
b = [4, 5, 6]      # Diagonal principal
c = [1, 1]         # Superdiagonal
d = [5, 10, 15]    # Vector del lado derecho

sol = crout_tridiagonal(a, b, c, d)
print("Solución:", sol)
