'''Escreva um programa em Python que leia os lados de n triângulos. Para cada triângulo
imprima a sua classificação quanto aos lados (equilátero, isósceles ou escaleno). O
programa deverá parar a execução quando o usuário digitar o valor zero para um dos
lados. Observação: para que os valores formem um triângulo é necessário que cada um
dos lados seja menor que a soma dos outros dois.'''

index = 1
while True:
    print (f"------------Triângulo {index}------------")
    a = int(input("Lado 1: "))
    b = int(input("Lado 2: "))
    c = int(input("Lado 3: "))
    
    if a == 0 or b == 0 or c == 0:
        break

    if a < b + c and b < c + a and c < a + b:
        if a == b == c:
            print("Triângulo Equilátero")
        elif a == b or b == c or c == a:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    else:
        print("Não é um triângulo")
    index += 1
    print()