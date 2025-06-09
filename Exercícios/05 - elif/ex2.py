from math import sqrt
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b**2 - 4*a*c
if delta >= 0:
    x1 = (-b + sqrt(delta)) / 2*a
    x2 = (-b - sqrt(delta)) / 2*a
    print(f"({x1:.2f},{x2:.2f})")
else:
    print("Valor inválido")

print(f"({x1:.2f},{x2:.2f})")