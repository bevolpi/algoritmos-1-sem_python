'''Escreva um programa em Python que leia um valor inteiro e positivo (o valor
deverá ser testado). O seu programa deverá imprimir no vídeo todos os divisores
inteiros do valor informado pelo usuário. A impressão dos valores deverá ser
feito em uma função.'''

def divisor ():
    for cont in range(-nm//2, nm//2 + 1): 
        if cont != 0 and nm % cont == 0:
            print(f"{cont}", end= " ")

nm = int(input("Insira um número inteiro e positivo: "))

if nm <= 0:
    print("Valor deve ser int e positivo")
else:
    print(-nm, end= " ")
    divisor()
    print(nm)



