lado1 = float(input("Insira o valor do lado 1: "))
lado2 = float(input("Insira o valor do lado 2: "))
lado3 = float(input("Insira o valor do lado 3: "))

if lado1 < lado2:
    aux = lado1
    lado1 = lado2
    lado2 = aux

if lado1 < lado3:
    aux = lado1
    lado1 = lado3
    lado3 = aux
    
if lado2 < lado3:
    aux = lado2
    lado2 = lado3
    lado3 = aux

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado2 + lado1):
    if lado1**2 == lado2**2 + lado3**2:
        print("É um triângulo retângulo")
    elif lado1**2 < lado2**2 + lado3**2:
        print("É um triângulo acutângulo")
    elif lado1**2 > lado2**2 + lado3**2:
        print("É um triângulo obtusângulo")
else: 
    print("Não é um triângulo")
