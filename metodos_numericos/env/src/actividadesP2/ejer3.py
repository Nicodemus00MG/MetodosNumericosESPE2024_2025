import numpy as np

def spline(x, y, x_interp):
    # Calcula los coeficientes de los splines cúbicos
    n = len(x) - 1
    h = np.diff(x)  # Diferencias entre puntos consecutivos en x
    b = np.diff(y) / h  # Diferencias divididas entre h (pendientes)

    # Matriz A para el sistema de ecuaciones
    A = np.zeros((n + 1, n + 1))
    A[0, 0] = 1  # Condición de frontera natural (segunda derivada en extremos es 0)
    A[n, n] = 1  # Condición de frontera natural

    for i in range(1, n):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]

    # Vector B para el sistema de ecuaciones
    B = np.zeros(n + 1)
    for i in range(1, n):
        B[i] = 3 * (b[i] - b[i-1])

    # Resuelve el sistema de ecuaciones para obtener los coeficientes c
    c = np.linalg.solve(A, B)

    # Calcula los coeficientes a, b, d
    a = y[:-1]
    b = b - h * (2 * c[:-1] + c[1:]) / 3
    d = (c[1:] - c[:-1]) / (3 * h)

    # Encuentra el intervalo adecuado para x_interp
    i = np.searchsorted(x, x_interp) - 1
    if i < 0:
        i = 0
    elif i >= n:
        i = n - 1

    # Calcula el valor interpolado y_interp
    dx = x_interp - x[i]
    y_interp = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
    
    return y_interp
