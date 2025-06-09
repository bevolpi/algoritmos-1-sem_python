'''Escreva um programa em python que leia os dados para um vetor de números
inteiros. Após o preenchimento do vetor, inverta a ordem dos elementos dentro
do próprio vetor e faça a impressão no vídeo.'''
import random

lista = []
def ler_dados():
    for i in range(5):
        lista.append(random.randint(1,30))
    print(lista)
    print(lista[:: -1])
    
ler_dados()