from math import sqrt
from math import pow

x = float(input("x = "))
'''
TÁ ERRADO!!!!!!!!!!!!!!!!!!!!!!!
y = (x - 8) / sqrt(pow(x,2) - 25) ----> a expressão precisa ta dentro do if!!!

if x <= 5:
    print("Não existente")
else:
    print(f"y = {y:.2f}")
'''

if x > 5 or x < -5:
    y = (x - 8) / sqrt(pow(x,2) - 25)
    print(f"y = {y:.2f}")
else:
    print("Valor inválido para x")

#podemos fazer o inverso tbm ---- COM AND!

if x <= 5 and x >= -5:
    print("Valor inválido para x")
else:
    y = (x - 8) / sqrt(pow(x,2) - 25)
    print(f"y = {y:.2f}")