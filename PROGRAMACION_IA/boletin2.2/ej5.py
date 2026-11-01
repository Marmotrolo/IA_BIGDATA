import numpy as np
import matplotlib.pyplot as plt


numeros= np.linspace(-2,2,20)

y=numeros**2

y2=numeros**3

plt.plot(numeros,y,marker="d", color="r", markerfacecolor="b")
plt.scatter(numeros,y2)
plt.grid()
plt.show()