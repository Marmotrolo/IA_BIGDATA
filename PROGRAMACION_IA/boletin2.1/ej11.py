import numpy as np
np.random.seed(73)
numcompetidores=15


dorsales=np.arange(numcompetidores)
dorsales=dorsales+1

np.random.shuffle(dorsales)

if len(numcompetidores)%2!=0:
    pasafase=dorsales[0]
    print("Pasa de pase:", pasafase)
    dorsales=dorsales[::1]
dorsales=dorsales.reshape(-1,2)
print(dorsales)