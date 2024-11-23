import numpy as np

# Datos
x = np.array([0, 8.46, 17.88, 27.31])
y = np.array([-93.33, -1.17, 0.41, 0.41])

# Ajustar un polinomio de grado 3
coefs = np.polyfit(x, y, 3)

# Imprimir los coeficientes
print("C3 =", coefs[0])
print("C2 =", coefs[1])
print("C1 =", coefs[2])
print("C0 =", coefs[3])