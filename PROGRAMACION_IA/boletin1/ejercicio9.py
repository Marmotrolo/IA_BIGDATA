numero1= 156
numero2= 89

sigue=True
while sigue==True:
    cociente=numero1//numero2
    resto=numero1%numero2
    if(resto==0):
        mcd=numero2
        sigue=False
    else:
        numero1=numero2
        numero2=resto

print("El mcd es:", mcd)
    