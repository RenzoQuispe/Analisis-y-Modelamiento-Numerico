import numpy as np

def diferencias_divididas(x, y):
    """
    Calcula la tabla de diferencias divididas y devuelve
    los coeficientes para el polinomio de Newton.
    
    Parámetros:
    x -- array con los valores x
    y -- array con los valores y
    
    Retorna:
    coef -- array con los coeficientes a_i
    """
    n = len(x)
    coef = np.copy(y).astype(float)
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    
    return coef

def polinomio_newton(coef, x_data, x):
    """
    Evalúa el polinomio de Newton en el punto x.
    
    Parámetros:
    coef -- coeficientes calculados con diferencias divididas
    x_data -- puntos x usados para construir el polinomio
    x -- valor o array donde se evalúa el polinomio
    
    Retorna:
    valor del polinomio en x
    """
    n = len(coef) - 1
    resultado = coef[n]
    for k in range(n - 1, -1, -1):
        resultado = resultado * (x - x_data[k]) + coef[k]
    return resultado

# Ejemplo con los datos dados
x_points = np.array([1, 3, 5, 6])
y_points = np.array([-3, 1, 2, 4])

coeficientes = diferencias_divididas(x_points, y_points)
print("Coeficientes del polinomio de Newton:")
print(coeficientes)

# Evaluar el polinomio en un punto, por ejemplo x=4
x_eval = 4
valor = polinomio_newton(coeficientes, x_points, x_eval)
print(f"Valor del polinomio en x = {x_eval}: {valor}")
