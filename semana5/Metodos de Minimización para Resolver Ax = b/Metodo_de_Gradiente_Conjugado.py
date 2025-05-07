import numpy as np

def gradiente_conjugado(A, b, x0, tol=1e-1, max_iter=100):
    x = x0
    r = b - A @ x
    p = r.copy()
    rs_old = np.dot(r, r)
    
    for i in range(max_iter):
        Ap = A @ p
        alpha = rs_old / np.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rs_new = np.dot(r, r)
        
        print(f"Iteración {i + 1}: x = {x}, r = {r}")
        
        if np.sqrt(rs_new) < tol:
            break
        
        beta = rs_new / rs_old
        p = r + beta * p
        rs_old = rs_new
    
    return x

# Ejemplo
A = np.array([[3, 1], [1, 2]])
b = np.array([1, 1])
x0 = np.array([0.0, 0.0])

sol = gradiente_conjugado(A, b, x0)
print("Solución aproximada:", sol)
