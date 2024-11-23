#CODIGO 1, ACTIVIDAD 3

def lagrange(x, y, x_interp):
    # Interpolación de Lagrange para encontrar el valor de y_interp para un valor de x_interp.
    # Parámetros:
    # x: lista de valores x conocidos
    # y: lista de valores y conocidos
    # x_interp: valor de x para el cual se desea interpolar un valor de y
    # Retorna:
    # y_interp: valor interpolado de y correspondiente a x_interp

    n = len(x)
    y_interp = 0
    for i in range(n):
        # Calcular el polinomio de Lagrange para la i-ésima entrada
        L = 1
        for j in range(n):
            if j != i:
                L *= (x_interp - x[j]) / (x[i] - x[j])
        y_interp += y[i] * L
    return y_interp