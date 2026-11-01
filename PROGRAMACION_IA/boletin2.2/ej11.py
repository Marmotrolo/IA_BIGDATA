import numpy as np
import matplotlib.pyplot as plt

datos=np.load('mapa.npz')

coord=datos['coordenadas']

valores=datos['valores']


x=coord[0]
y=coord[1]




plt.scatter(x,y,cmap='viridis', s=valores*20,c=valores,alpha=1-valores/10)

plt.show()