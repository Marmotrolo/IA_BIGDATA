import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(0,10,10)

y=np.sin(x)

plt.plot(x,y, color="#E0616C", linewidth=5, marker='D', markersize="10")
plt.show()