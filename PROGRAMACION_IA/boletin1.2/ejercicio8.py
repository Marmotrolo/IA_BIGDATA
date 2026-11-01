frase="Hola tengo 19 años, 1 gato y 8 primos"
fraseseparada=frase.split()


numerosenfrase=[c for c in fraseseparada if c.isdigit()]

print(numerosenfrase)