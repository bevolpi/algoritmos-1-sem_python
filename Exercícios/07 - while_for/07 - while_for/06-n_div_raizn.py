'''Desenvolva um programa que calcule o valor da expressão: y = 1/raiz1 + 2/raiz2 ... + n/raizn'''
from math import sqrt

nm = int(input("Insira um número inteiro: "))
cont = 1
total = 0
while cont <= nm:
    total = total + cont/sqrt(cont)
    cont = cont + 1
print(total)

# ou
tt = 0 
nm = int(input("Insira um número inteiro: "))
for cont in range(1, nm+1):
    tt = tt + cont/sqrt(cont)
    cont += 1
print(tt)  
