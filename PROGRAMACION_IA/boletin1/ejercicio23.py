palabrasecreta="LAGARTIJA"

palabrasecretalista=list(palabrasecreta)
longitud=len(palabrasecretalista)
adivina=["_"]*longitud
intentos=10

while adivina != palabrasecreta and intentos!=0:
    print(adivina)
    intento=input("Dime una letra:")

    if(intento not in palabrasecreta ):
        intentos=intentos-1
        print("Fallaste, intentos restantes:",intentos)
    elif(intento not in adivina  ):
        for i,letra in enumerate(palabrasecretalista) :
            if letra==intento:
                adivina[i]=intento
    