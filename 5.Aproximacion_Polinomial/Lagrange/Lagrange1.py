def lagrange_interpolation(x_points, y_points, x):
    """
    Calcula el valor interpolado en x usando el polinomio de Lagrange.

    :param x_points: lista de valores x conocidos
    :param y_points: lista de valores y conocidos (correspondientes a x_points)
    :param x: valor donde se quiere interpolar
    :return: valor interpolado en x
    """
    total = 0
    n = len(x_points)

    for i in range(n):
        xi, yi = x_points[i], y_points[i]

        # Calcular el polinomio base L_i(x)
        Li = 1
        for j in range(n):
            if j != i:
                xj = x_points[j]
                Li *= (x - xj) / (xi - xj)

        total += yi * Li

    return total

# Ejemplo de uso
x_pts = [1, 2, 4]
y_pts = [2, 3, 1]

valor = 3  # interpolar en x=3
resultado = lagrange_interpolation(x_pts, y_pts, valor)
print(f"El valor interpolado en x={valor} es {resultado:.4f}")
