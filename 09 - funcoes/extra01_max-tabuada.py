'''Escreva um programa em Python que preencha um vetor (lista) de 10 posições com
valores inteiros e aleatórios. Em seguida, imprima no vídeo a tabuada do maior valor
armazenado no array. O programa deverá ter uma função para determinar o maior
valor armazenado na lista e outra função para imprimir a tabuada.'''

import random
def preencher():
    for i in range(10):
        lista.append(random.randint(1, 20))

# def imprimir_max():
#     for i in range(len(lista)):
#         for i in range(len(lista) - 1):
#             if i == 0 or lista[i] > lista[i+1]:
#                 maior = lista[i]
#                 lista[i] = lista[i+1]
#                 lista[i+1] = maior
#         return maior         --------------> esse dá certo tbm

def imprimir_max():
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior
        
def imprimir_tabuada(nm):
    for i in range(1,11):
        print(f"{nm} x {i} = {nm * i}")

lista = []

preencher()
print(f"Lista: {lista}")

maior = imprimir_max()
print(f"Maior elemento da lista: {maior}")

print(f"Tabuada de {maior}, o maior número:")
imprimir_tabuada(maior) #atribuí que ele vai chamar o nm com o número ENCONTRADO NO IMPRIMIR_MAX!

