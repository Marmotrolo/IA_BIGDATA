import numpy as np

ventas = np.array([100, 200, 50, 80, 150])

iva = ventas * 0.21
restante = ventas - iva
beneficio = restante * 0.10
compras = restante - beneficio

print("Ventas:", ventas)
print("IVA:", iva)
print("Beneficio:", beneficio)
print("Dinero para nuevos productos:", compras)