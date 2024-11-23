#! importacion de librerias a usar 
import numpy as np 
import matplotlib.pyplot as plt

# ! Definicion de las  funcion f , este retorna sin(x)*cos(x) en funcion de los campos de parametros obtenidos 
def f(x):
    return np.sin(x) * np.cos(x)

# ! definir el rango de -pi a pi pero con 25 puntos totales 
x = np.linspace(-np.pi, np.pi, 25) #
#! defino en si y que es igual al retorno de la funcion f , donde este recibe por parametro x  , y x es la tabla  de 25 valores obtenidos 
y = f(x)

#! definicion del tamaño del canva
plt.figure(figsize=(12, 8))

# ! Definicion del plot y dar atributos al objeto , entre estos , principalmente el plot recibe por parametros x e y 

#*** Ademas este se complementa con los atributos de entrada de tipo label , y este es un campo para titular o documentar, 
# ? label , corresponde a la ecuacion definida f(x)= sin(x) cos(x), en funcion de un dominio de -pi<=x<=pi
plt.plot(x, y, label=r'$f(x) = \sin(x) \cos(x), \ x \in [-\pi, \pi]$', color='red')

# ! Dar titulos y descripciones al plot 
plt.title(r'$f(x) = \sin(x) \cos(x), \ x \in [-\pi, \pi]$', loc='left', fontsize=14)
plt.title('Nicolás Muñoz', loc='right', fontsize=14)
plt.xlabel('x')
plt.ylabel('f(x)')

# ! Definición de la grilla y configuracion generica 
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.minorticks_on()

#! Mostrar el plot (o la grafica f(x))
plt.legend()
plt.show()