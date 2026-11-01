import numpy as np

a=np.array([1,10,2,11,3,12])

print(a)

b=np.zeros((2,4),int)
print(b)

c=np.full((4,3),2)
print(c)

d=np.full((5,1), 99)
print(d)

e=np.arange(0,101,5)
print(e)

f=np.linspace(0,1,5)
print(f)

g=np.zeros((5,7), np.int8)
g[1,2]=3
print(g)