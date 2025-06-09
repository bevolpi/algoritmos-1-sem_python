lado1 = float(input("Escreva valor do lado 1: "))
lado2 = float(input("Escreva valor do lado 2: "))
lado3 = float(input("Escreva valor do lado 3: "))

if (lado1 < lado2 + lado3) and (lado2 < lado3 + lado1) and (lado3 < lado1 + lado2):
    print("É um triângulo")
else:
    print("Não é um triângulo")