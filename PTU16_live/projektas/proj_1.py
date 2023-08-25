import matematika as mat
from math import sqrt

print(mat.pasisveikinti("Penktadieninis"))
penki = sqrt(25)
print(penki)
klase = mat.ManoKlase(penki)
print(klase.kvadratas())
print(mat.sudetis(klase.x, penki))
