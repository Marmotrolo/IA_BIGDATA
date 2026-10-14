
def anagramas(*palabras):
        longitud=len(palabras)
        palabrasanagrama=[]
        for i in range(longitud):
            palabra=palabras[i]
            palabraalreves= palabra[::-1]
            for j in range(i+1):
                palabracomparar=palabras[j]
                palabra1=sorted(palabra)
                palabra2=sorted(palabracomparar)
                if(palabra1==palabra2 not in palabrasanagrama):
                    palabrasanagrama.append(palabracomparar)
        return palabrasanagrama
                
    


print(anagramas("amor","jamon","arroz","roma","ruiz","monja"))