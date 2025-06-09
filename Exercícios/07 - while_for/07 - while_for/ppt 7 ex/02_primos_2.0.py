'''Escreva um programa em Python que leia dois valores inteiros e positivos representando o
início e o fim de um intervalo de números. Imprima todos os números primos no intervalo
formado pelos números informados pelo usuário'''

inicio = int(input("Insira o primeiro nm: ")) # 5
fim = int(input("Insira o segundo nm: ")) # 7

if inicio <= 0 or  fim <= 0:
    print("Os nms devem ser MAIOR que zero: ")
else:
    for nm in range(inicio, fim+1): # 5 6 7
        tt_divisores = 0
        for divisor in range(1, nm+1): # 1 2 3
            if nm % divisor == 0:
                tt_divisores = tt_divisores + 1
        if tt_divisores == 2:
            print(nm, end= " ")
            
#EXPLICAÇÃO:
if inicio <= 0 or  fim <= 0:
    print("Os nms devem ser MAIOR que zero: ")
else:
    for i in range(inicio, fim+1): # 5 6 7
        tt_divisores = 0
# p ser primo, deve ter somente 2 divisores, por 1 e por ele mesmo!
        for j in range(1, i+1): # 1 2 3
            if i % j == 0:
# 1° faz 5 % 1, se for vdd, adiciona 1 no tt_div. + volta p inicio do for,
# se não só volta. E continua... 5 % 2, 5 % 3 EEEEEE 6 % 1...
                tt_divisores = tt_divisores + 1
        if tt_divisores == 2:
            print(i, end= " ")