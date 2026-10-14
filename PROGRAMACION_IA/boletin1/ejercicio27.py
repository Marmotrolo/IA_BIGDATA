nombre=input("Dime tu nombre y apellidos")

listanombreennumeros=[ord(i.lower())-96 for i in nombre if i != " "]

longitud=len(listanombreennumeros)
print(listanombreennumeros)

numerodelasupersuerte= list()

setsupersuerte= set()
#CON LIST
for i in range(longitud):
    for j in range(i+1,longitud):
        valordei= listanombreennumeros[i]
        valordej=listanombreennumeros[j]
        if valordei==valordej and valordei not in numerodelasupersuerte:
            numerodelasupersuerte.append(valordei)
print(numerodelasupersuerte)

#con SET
for x in listanombreennumeros:
    if listanombreennumeros.count(x)>1 and x not in setsupersuerte:
        setsupersuerte.add(x)
print(setsupersuerte)

