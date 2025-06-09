'''Escreva um programa em Python, contendo uma função que calcule e retorne o
valor da expressão:
y = (5*x + 3) / sqrt((x**2) - 16)'''

from math import sqrt
def calcular(x):
    if x < 4:
        return "Sem raíz real"
    elif x == 4:
        return "Divisão por 0"
    else:
        y = (5*x + 3) / sqrt((x**2) - 16)
        return y

x = float(input("x = "))
y = calcular(x)
 
print(f"y = {y}")