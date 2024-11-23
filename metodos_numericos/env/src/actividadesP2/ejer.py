# Librerías
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Configurar el backend de matplotlib
import matplotlib
matplotlib.use('Agg')

# Definir la variable simbólica
x = sp.Symbol('x')

# Definir la función seno simbólica
f = sp.sin(x)

# Crear un rango de valores para x
x_vals = np.linspace(-2*np.pi, 2*np.pi, 100)

# Evaluar la función simbólica en los valores de x
y_vals = [f.subs(x, val).evalf() for val in x_vals]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals)
plt.title('Gráfica de la función seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.show()

# Guardar la gráfica como imagen
#plt.savefig('seno_grafica.png')

print("Gráfica de seno creada exitosamente y guardada como 'seno_grafica.png'")