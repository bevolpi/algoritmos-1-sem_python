from math import sqrt
from math import pow

xa = float(input("xa = "))
xb = float(input("xb = "))
ya = float(input("ya = "))
yb = float(input("yb = "))

distanciaa= sqrt((0 - xa)**2 + (0 - ya)**2)
distanciab= sqrt((0 - xb)**2 + (0 - yb)**2)

print(f"A = {xa}, {ya}")
print(f"B = {xb}, {yb}")

if (distanciaa) < (distanciab):
    print(f"O mais próximo ao (0,0) é {(xa,ya)}")
else:
    print(f"O mais próximo ao (0,0) é {(xb,yb)}")