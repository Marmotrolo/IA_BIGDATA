import numpy as np

ventas = np.array([100, 200, 50, 80, 150])

iva = ventas * 0.21
restante =np.subtract(ventas,iva)
beneficio = restante * 0.10
compras = np.subtract(restante,beneficio)

print("Ventas:", ventas)
print("IVA:", iva)
print("Beneficio:", beneficio)
print("Dinero para nuevos productos:", compras) 