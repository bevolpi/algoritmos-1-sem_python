from math import sqrt
a = float(input("Informe o valor de a (diferente de 0): "))

if a == 0:
    print("não é uma equação de 2° grau")
else: 
    b = float(input("Informe o valor de b: "))
    c = float(input("Informe o valor de c: "))
    delta = b** 2 - 4*a*c
    if delta < 0:
        print("a equação não tem raiz real")
    else:
            x1 = (-b + sqrt(delta)) / 2*a
            x2 = (-b - sqrt(delta)) / 2*a
            print(f"({x1:.2f},{x2:.2f})")