import numpy as np
import matplotlib.pyplot as plt

pasos = 100
# Genera 1 o -1 de forma aleatoria para cada paso
movimientos = np.random.choice([-1, 1], size=pasos)
# Acumula los movimientos para obtener la posición en cada instante
posicion = np.cumsum(movimientos)

plt.plot(posicion)
plt.title("Caminata Aleatoria Optimizada")
plt.show()
