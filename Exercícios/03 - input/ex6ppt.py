import math

x = float(input("Escreva o valor de X: "))
a = 1/2

z = x - a
r = z ** (1/3)
y = r ** (1/2)
# y = math.sqrt(math.cbrt(x - a))

print(f"y = {y:.3f}")