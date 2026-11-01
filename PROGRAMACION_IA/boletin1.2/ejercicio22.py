import numpy.random

numerosaleatorios= numpy.random.randint(1,1000,100) 
numerosrepetidos=[c for c in numerosaleatorios if list(numerosaleatorios).count(c)>1]
sigue=True

numerospares= [c for c in numerosaleatorios if c]

numerosimpares= [c for c in numerosaleatorios if c%3==0]

print(numerospares)
print("----------------------------------------------")
print(numerosimpares)
print("----------------------------------------------")
print(numerosrepetidos)