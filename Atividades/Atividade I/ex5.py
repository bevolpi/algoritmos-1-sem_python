lado1 = float(input("Insira o valor do lado 1: "))
lado2 = float(input("Insira o valor do lado 2: "))
lado3 = float(input("Insira o valor do lado 3: "))

if (lado1 > lado2 and lado1 > lado3) and (lado1 < lado2 + lado3):
    a = lado1
    b = lado2
    c = lado3
    if a**2 == b**2 + c**2:
        print("É um triângulo retângulo")
    elif a**2 < b**2 + c**2:
        print("É um triângulo acutângulo")
    elif a**2 > b**2 + c**2:
        print("É um triângulo obtusângulo")
elif (lado2 > lado3 and lado2 > lado1) and (lado2 < lado3 + lado1):
    a = lado2
    b = lado3
    c = lado1
    if a**2 == b**2 + c**2:
        print("É um triângulo retângulo")
    elif a**2 < b**2 + c**2:
        print("É um triângulo acutângulo")
    elif a**2 > b**2 + c**2:
        print("É um triângulo obtusângulo")
elif (lado3 > lado1 and lado3 > lado2) and (lado3 < lado1 + lado2):
    a = lado3
    b = lado1
    c = lado2
    if a**2 == b**2 + c**2:
        print("É um triângulo retângulo")
    elif a**2 < b**2 + c**2:
        print("É um triângulo acutângulo")
    elif a**2 > b**2 + c**2:
        print("É um triângulo obtusângulo")
else:
    print("Não é um triângulo")
