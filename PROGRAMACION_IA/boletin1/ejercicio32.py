frase="Las Ventanas son rojas y las puertas tambien son rojas "

palabras=frase.lower().split()

palabrasset=set(palabras)

palabraslista=list(palabrasset)

palabraslista.sort()
print(palabraslista)