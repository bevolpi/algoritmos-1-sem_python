'''Escreva um programa em Python que leia um vetor (lista) de 10 posições com
valores inteiros e aleatórios. Em seguida, coloque os elementos do vetor em ordem
crescente. O programa deverá ter uma função para preencher a lista, uma função
para ordenar a lista e outra função para fazer a impressão dos elementos da lista.'''

import random
def preencher():
    for i in range(10):
        lista.append(random.randint(1, 20))

def ordenar():
    for _ in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                
def imprimir():
    for i in range(len(lista)):
        print(lista[i], end= " ")

lista = []
preencher()
print(f"\nDados antes da ordenação")
imprimir()
print(f"\nDados depois da ordenação")
ordenar()
imprimir()