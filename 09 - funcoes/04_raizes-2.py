'''Escreva um programa em Python para calcular as raízes de uma equação do
segundo grau. O seu programa deverá ter uma função para calcular e retornar o
valor do delta e também uma função para calcular e retornar as duas raízes da
equação.'''

from math import sqrt
def delta():
    deltinha = (b**2) - 4 * a * c
    return deltinha

def raizes():
    x1 = (-b + sqrt(deltinha)) / (2 * a)
    x2 = (-b - sqrt(deltinha)) / (2 * a)
    return x1, x2

a = float(input("a = "))
if a == 0:
    print("Não é uma equação do 2° grau")
else:
    b = float(input("b = "))
    c = float(input("c = "))
    deltinha = delta()
    if delta < 0:
        print("A equação não tem raiz real")
    else:
        x1, x2 = raizes() #só funciona no PY -> nas outras precisa fazer 2 def
        print(f"x1 = {x1:2f}")
        print(f"x2 = {x2:2f}")

# meu jeito
def delta():
    deltinha = (b**2) - 4 * a * c
    return deltinha

def raizes():
    xa = (-b + sqrt(deltinha)) / (2 * a)
    xb = (-b - sqrt(deltinha)) / (2 * a)
    print(f"({xa},{xb})")

a = float(input("a = "))
if a == 0:
    print("Não é uma equação do 2° grau")
else:
    b = float(input("b = "))
    c = float(input("c = "))
    deltinha = delta()
    if deltinha < 0:
        print("A equação não tem raiz real")
    else:
        raizes()
