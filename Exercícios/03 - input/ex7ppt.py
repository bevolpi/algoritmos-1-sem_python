from math import sqrt
from math import pow

x = float(input("Digite o valor de x: "))

# 3 maneiras de fazer!
'''
a = x ** 4
b = x ** 2
z = ((a - 1) / (2 * b)) ** 2
r = (1 + z) ** (1/2)
y = r - b/2
'''

y = sqrt(1 + ((pow(x,4) - 1) / (2 * pow(x,2))) ** 2) - (pow(x,2) / 2)

'''
a = ((pow(x,4) - 1) / (2 * pow(x,2))) ** 2
b = sqrt (1 + a)
c = pow(x,2) / 2
y = b - c
'''

print(f"Resultado: {y:.3f}")