import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Definir las funciones para cada término y la solución
def y(x):
    return 2/x

def dy_dx(x):
    return -2/(x**2)

def term1(x):
    return -6 * np.ones_like(x)

def term2(x):
    return 48 / (x**4)

def term3(x):
    return -4 / x

def total_sum(x):
    return term1(x) + term2(x) + term3(x)

# Configurar el estilo de la gráfica
plt.style.use('default')
plt.rcParams.update({
    'font.size': 12,
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman'],
})

# Crear la figura y los subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16))
fig.suptitle(r'Verificaci\'on de la soluci\'on $y = \frac{2}{x}$', fontsize=20)

# Generar datos
x = np.linspace(0.1, 10, 1000)

# Primera gráfica: Solución y su derivada
plot1 = ax1.plot(x, y(x), label=r'$y = \frac{2}{x}$', color='blue')
plot2 = ax1.plot(x, dy_dx(x), label=r'$\frac{dy}{dx} = -\frac{2}{x^2}$', color='red')
ax1.set_title(r'Soluci\'on $y = \frac{2}{x}$ y su derivada')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.legend()
ax1.grid(True, which='both', linestyle='--', color='gray', alpha=0.7)

# Añadir colorbar a la primera gráfica
divider1 = make_axes_locatable(ax1)
cax1 = divider1.append_axes("right", size="5%", pad=0.05)
sm1 = plt.cm.ScalarMappable(cmap='coolwarm', norm=colors.Normalize(vmin=min(y(x)), vmax=max(y(x))))
sm1.set_array([])
fig.colorbar(sm1, cax=cax1, label='Valor de $y$')

# Segunda gráfica: Términos de la ecuación verificada
terms = [term1, term2, term3, total_sum]
labels = [r'$-6$', r'$\frac{48}{x^4}$', r'$-\frac{4}{x}$', 'Suma total']
cmap = plt.get_cmap('viridis')
colors_list = [cmap(i) for i in np.linspace(0, 1, len(terms))]

for term, color, label in zip(terms, colors_list, labels):
    ax2.plot(x, term(x), label=label, color=color)

ax2.set_title(r'T\'erminos de la ecuaci\'on $-6 + \frac{48}{x^4} - \frac{4}{x} = 0$')
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.legend()
ax2.grid(True, which='both', linestyle='--', color='gray', alpha=0.7)

# Ajustar el rango del eje y para mejor visualización
ax2.set_ylim(-10, 10)

# Añadir una línea horizontal en y=0 para referencia
ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)

# Añadir colorbar a la segunda gráfica
divider2 = make_axes_locatable(ax2)
cax2 = divider2.append_axes("right", size="5%", pad=0.05)
sm2 = plt.cm.ScalarMappable(cmap='viridis', norm=colors.Normalize(vmin=min(total_sum(x)), vmax=max(total_sum(x))))
sm2.set_array([])
fig.colorbar(sm2, cax=cax2, label='Valor de los t\'erminos')

# Ajustar el diseño
plt.tight_layout()

# Mostrar la gráfica
plt.show()