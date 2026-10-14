nombreyapellidos=input("Dime nombre y apellidos")
nombreyapellidossinespacios=nombreyapellidos.replace(" ","_")
usuario=nombreyapellidossinespacios[:4]+nombreyapellidossinespacios[-3:]
print(usuario.lower())