import numpy as np

bombo=np.arange(1,50)
misnumeros=np.random.permutation(bombo)[0:6]


numerosacierto=0
intentos=0
while numerosacierto <2:
    intentos=intentos+1
    numerosganadores=np.random.permutation(bombo)[0:6]
    numerosacierto= np.isin(misnumeros,numerosganadores).sum()
        

print("Has acertado a la", intentos)
print(numerosganadores, misnumeros)
