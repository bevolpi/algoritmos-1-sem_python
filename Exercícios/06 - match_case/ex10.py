'''Escreva um programa em Python que leia três números (possíveis lados de um triângulo).
Imprima sua classificação quanto aos lados:
 Três lados iguais equilátero.
 Dois lados iguais isósceles.
 Três lados diferentes escaleno.'''

a = int(input("lado 1 = "))
b = int(input("lado 2 = "))
c = int(input("lado 3 = "))

if a > b + c or b > b + c or c > a + b:
    print("Não é um triângulo")
else:
    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or b == c or c == a:
        print("Triângulo isósceles")
    else: 
        print("Triângulo escaleno")