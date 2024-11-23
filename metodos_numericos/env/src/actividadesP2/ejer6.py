import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definición del sistema de ecuaciones
def system(y, t):
    z, z1, z2 = y
    dz2dt = 4*z2 + 75*z1 - 378*z
    return [z1, z2, dz2dt]

# Condiciones iniciales
y0 = [1, 0, 0]

# Rango de tiempo
t = np.linspace(0, 1, 1000)

# Solución "exacta" usando odeint de SciPy
sol_exact = odeint(system, y0, t)

# Método de Euler
def euler(f, y0, t):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        h = t[i+1] - t[i]
        y[i+1] = y[i] + h * np.array(f(y[i], t[i]))
    return y

# Método RK4
def rk4(f, y0, t):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        h = t[i+1] - t[i]
        k1 = np.array(f(y[i], t[i]))
        k2 = np.array(f(y[i] + k1 * h/2, t[i] + h/2))
        k3 = np.array(f(y[i] + k2 * h/2, t[i] + h/2))
        k4 = np.array(f(y[i] + k3 * h, t[i+1]))
        y[i+1] = y[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y

# Método Adams-Bashforth (4-paso)
def adams_bashforth(f, y0, t):
    n = len(t)
    y = np.zeros((n, len(y0)))
    # Usar RK4 para los primeros 4 puntos
    y[:4] = rk4(f, y0, t[:4])
    for i in range(3, n - 1):
        h = t[i+1] - t[i]
        y[i+1] = y[i] + (h/24) * (55*np.array(f(y[i], t[i])) - 59*np.array(f(y[i-1], t[i-1])) 
                                  + 37*np.array(f(y[i-2], t[i-2])) - 9*np.array(f(y[i-3], t[i-3])))
    return y

# Calcular soluciones
sol_euler = euler(system, y0, t)
sol_rk4 = rk4(system, y0, t)
sol_ab = adams_bashforth(system, y0, t)

# Graficar resultados
plt.figure(figsize=(12, 8))
plt.plot(t, sol_exact[:, 0], 'k-', label='Exacta (odeint)')
plt.plot(t, sol_euler[:, 0], 'r--', label='Euler')
plt.plot(t, sol_rk4[:, 0], 'g-.', label='RK4')
plt.plot(t, sol_ab[:, 0], 'b:', label='Adams-Bashforth')
plt.xlabel('t')
plt.ylabel('z(t)')
plt.title('Comparación de métodos numéricos')
plt.legend()
plt.grid(True)
plt.show()

# Análisis de errores
def error_rms(sol, sol_exact):
    return np.sqrt(np.mean((sol[:, 0] - sol_exact[:, 0])**2))

print(f"Error RMS Euler: {error_rms(sol_euler, sol_exact)}")
print(f"Error RMS RK4: {error_rms(sol_rk4, sol_exact)}")
print(f"Error RMS Adams-Bashforth: {error_rms(sol_ab, sol_exact)}")