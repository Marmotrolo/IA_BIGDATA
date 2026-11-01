import numpy as np
import matplotlib.pyplot as plt

datos = np.array([10, 20, 40, 15])
alimentos = np.array(["trigo", "aceituna", "papa", "zanahoria"])

# 1. Obtener los índices que ordenarían los datos de menor a mayor
indices_ordenados = np.argsort(datos)

# 2. Reordenar ambos arrays usando esos índices
datos_ordenados = datos[indices_ordenados]
alimentos_ordenados = alimentos[indices_ordenados]


plt.pie(datos_ordenados, labels=alimentos_ordenados, explode= [0.05]*len(datos))

plt.show()
