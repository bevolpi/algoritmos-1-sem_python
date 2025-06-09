'''Escreva um programa em Python que leia três valores. Caso os valores formem os
lados de um triângulo, imprima a sua classificação quanto aos lados. Observação:
para que três valores formem os lados de um triângulo é necessário que cada
um dos lados seja menor que a soma dos outros dois. A classificação dos
triângulos quanto aos lado é: equilátero (3 lados iguais), isósceles (2 lados iguais)
ou escaleno (3 lados diferentes).'''

def classificar():
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or b == c or c == a:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

        
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < b + c and b < c + a and c < a + b:
    classificar()
else:
    print("Não é um triângulo")