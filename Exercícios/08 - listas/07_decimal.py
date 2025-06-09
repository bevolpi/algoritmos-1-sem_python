'''Escreva um programa em python que leia um valor inteiro e positivo na base de
numeração decimal. Faça a conversão para binária e imprima o valor convertido
no vídeo'''

decimal = int(input("Insira um valor inteiro e positivo: "))

if decimal < 0:
    print("O valor precisa ser POSITIVO")
else:
    if decimal == 0:
        print("O valor 0 em binário é: 0")
    else:
        binario = []
        n = decimal
        while n > 0:
            resto = n % 2
            binario.append(resto)
            n = n // 2
        print(f"O valor {decimal} em binário é: ", end="")
        i = len(binario) - 1
        while i >= 0:
            print(binario[i], end="")
            i = i - 1
        print()