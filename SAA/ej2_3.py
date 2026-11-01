import scipy.stats as st

muestra=1000
mu=176
sigma=10

cmbuscados=170

#tipificamos

z=(170-176)/sigma


probabilidadpersonasmasde170=st.norm.cdf(z)

print(probabilidadpersonasmasde170)


