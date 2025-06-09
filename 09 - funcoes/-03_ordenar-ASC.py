'''programa para preencher uma lista com 10 numeros inteiros e 
colocar em ordem crescente - ordenar é comparar os elementos e trocar eles'''

import random 

def ler_dados():
    for i in range(10):
        lista.append(random.randint(20, 40))

def imprimir():
    for i in range(len(lista)):
        print(lista[i], end=" ")    

def ordenar():
    for o in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                
# principal
lista = []
ler_dados()
print("\nDados antes da ordenação")
imprimir()
ordenar()
print("\nDados após a ordenação")
imprimir()