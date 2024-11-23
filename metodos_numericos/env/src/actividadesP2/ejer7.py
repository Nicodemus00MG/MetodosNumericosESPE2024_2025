import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title(r'$\sin(x)$ function')
plt.xlabel(r'$x$')
plt.ylabel(r'$\ sin(x)$')
plt.text(0, 0, r'$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$', fontsize=15)
plt.grid(True)
plt.show()