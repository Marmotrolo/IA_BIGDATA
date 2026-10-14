a=5
b=5
listanumeros=(a,b)
sumanumeros=0
for posicion in range(len(listanumeros)):
    numero=listanumeros[posicion]
    sumanumeros+= numero
suma= sumanumeros
print(suma/(len(listanumeros)))