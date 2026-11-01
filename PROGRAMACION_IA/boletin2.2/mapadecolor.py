import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)  # Tercera variable que define el color

# Gráfico de dispersión con mapa de colores
plt.scatter(x, y, c=z, cmap='viridis')

# Añadir barra de color (color bar)

plt.show()
