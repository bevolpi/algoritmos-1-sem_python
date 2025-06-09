'''Escreva um programa em python que preencha um vetor de 1000 posições
com valores fornecidos pelo usuário. Imprima no vídeo o maior e o menor
valor armazenado'''

from math import inf

lista = []
maior = 0
#menor = 0 -> esse tá certo tbm!
menor = inf
for i in range(5):
    lista.append(int(input("iNSIRA OS VALORES")))
    if i == 0 or lista[i] > maior: #i==0, pq se não maior=0 em resp negativa fica como resp!
        maior = lista[i]
    # if i == 0 or lista[i] < menor: 
    #     menor = lista[i]
    if lista[i] < menor: 
        menor = lista[i]
    
print(lista)
print()
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")