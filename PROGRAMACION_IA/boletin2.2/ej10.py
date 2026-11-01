import numpy as np
import matplotlib.pyplot as plt

coord=np.random.randint(0,101,size=(2,15))
valores=np.random.randint(0,11, size=(1,15))



print(coord)
print(valores)

np.savez("mapa.npz",coordenadas=coord, valores=valores)

