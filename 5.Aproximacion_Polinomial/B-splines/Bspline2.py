import numpy as np
import matplotlib.pyplot as plt

def cox_de_boor(t, i, k, knots):
    """
    Evalúa recursivamente la función base B-spline N_{i,k}(t)
    """
    if k == 1:
        return 1.0 if knots[i] <= t < knots[i+1] else 0.0
    denom1 = knots[i + k - 1] - knots[i]
    denom2 = knots[i + k] - knots[i + 1]
    term1 = 0.0
    term2 = 0.0
    if denom1 > 0:
        term1 = ((t - knots[i]) / denom1) * cox_de_boor(t, i, k - 1, knots)
    if denom2 > 0:
        term2 = ((knots[i + k] - t) / denom2) * cox_de_boor(t, i + 1, k - 1, knots)
    return term1 + term2

def plot_b_spline_basis(n=4, k=3, knot_vector=None, resolution=1000):
    """
    Dibuja las funciones base B-spline para n+1 funciones de base y orden k.
    """
    if knot_vector is None:
        knot_vector = np.arange(n + k + 1)
    t_vals = np.linspace(knot_vector[0], knot_vector[-1], resolution)
    basis_values = np.zeros((n+1, len(t_vals)))

    for i in range(n+1):
        for j, t in enumerate(t_vals):
            basis_values[i, j] = cox_de_boor(t, i, k, knot_vector)

    plt.figure(figsize=(10, 6))
    for i in range(n+1):
        plt.plot(t_vals, basis_values[i], label=f'$N_{{{i},{k}}}(t)$')

    plt.title(f'Funciones Base B-spline de orden {k}')
    plt.xlabel('$t$')
    plt.ylabel('$N_{i,k}(t)$')
    plt.grid(True)
    plt.legend()
    plt.show()

# Ejecutar la función con n = 3 y vector de nudos [0,1,2,3,4,5,6]
plot_b_spline_basis(n=3, k=3, knot_vector=[0, 1, 2, 3, 4, 5, 6])
