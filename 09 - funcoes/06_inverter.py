'''Escreva um programa em Python que:
a) preencha um vetor de 10 posições com valores aleatórios (o preenchimento
deverá ser feito por uma função).
b) Imprima os dados do vetor no vídeo (a impressão deverá ser feita por uma
função).
c) Faça a inversão dos valores do vetor (a inversão deverá ser feita por uma função).
d) Imprima novamente o vetor no vídeo para ter certeza que a inversão ocorreu
corretamente.'''

#a) 
import random
def preencher():
    for i in range(10):
        lista.append(random.randint(1, 20))

#b)
def imprimir():
    for i in range(len(lista)):
        print(lista[i], end= " ")

#c)
def inverter():
    n = len(lista)
    for i in range(n // 2):
        aux = lista[i]
        lista[i] = lista[n - i - 1]
        lista[n - i - 1] = aux
            
            

lista = []
preencher()
print("Antes")
imprimir()
print("\nDepois")
inverter()
imprimir()