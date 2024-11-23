import numpy as np
import matplotlib.pyplot as plt

# tabulacion de datos (dominio exitencial)
X = np.array([50, 52, 54, 56, 58, 60, 62])
Y = np.array([31, 50, 77, 96, 112, 130, 162])

# logaritmo natural , uso de numpy
Y_log = np.log(Y)

#! uso de la funcion sen(x)
Y_sen= np.sin(Y)

# Cálculo de las sumatorios 
n = len(X)
sum_X = np.sum(X)
sum_Y_sen = np.sum(Y_sen)
sum_X2 = np.sum(X**2)
sum_XY_log = np.sum(X * Y_sen)

# Resolucion de sistema de ecuaciones , tanto para A y B
A = (n * sum_XY_log - sum_X * sum_Y_sen) / (n * sum_X2 - sum_X**2)
B = (sum_Y_sen * sum_X2 - sum_X * sum_XY_log) / (n * sum_X2 - sum_X**2)

# sustitucion al modelo original exponencial
a = np.exp(B)
b = A

# Generar la curva ajustada usando los parámetros obtenidos
Y_fit = a * np.exp(b * X)

# Graficar los datos originales y el ajuste exponencial con formato solicitado
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, label="Datos Originales", color="red")
plt.plot(X, Y_fit, label=r'$y = sen(ax)$' + f'\n$a = {a:.4f}$, $b = {b:.4f}$', color="blue")

# Configuración de la grilla
plt.grid(which='both')
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
plt.axhline(0, color="black")
plt.axvline(0, color="black")

# Títulos y etiquetas
plt.title(r'$y = ae^{bx}$', loc='left', fontsize=14)  # Título a la izquierda
plt.title('Autor: Josue Muñoz', loc='right', fontsize=14)  # Título a la derecha
plt.xlabel('Eje X')  # Etiqueta del eje X
plt.ylabel('Eje Y')  # Etiqueta del eje Y

# Leyenda
plt.legend(loc='upper left')

# Límites de los ejes
plt.xlim(min(X)-5, max(X)+5)
plt.ylim(min(Y)-10, max(Y)+50)

plt.show()

# Calcular y verificar el valor para X = 64
X_new = 64
Y_new = a * np.exp(b * X_new)
print(f"El valor predicho de Y para X = {X_new} es: {Y_new:.4f}")
