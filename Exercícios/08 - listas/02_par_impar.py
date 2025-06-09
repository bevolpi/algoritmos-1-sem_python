'''Escreva um programa em python que preencha um vetor de 1000 posições
com valores fornecidos pelo usuário. Imprima no vídeo a quantidade de
números pares e ímpares digitados e a porcentagem de pares e ímpares.'''

lista = []
par = 0
impar = 0
#tt = 0 -> não necessariamente precisa dessa variável
for i in range(5):
    lista.append(int(input("iNSIRA OS VALORES")))
    if lista[i] % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    # tt = tt + 1

print(par)
print(impar)
#par = par*100/tt
par = par / len(lista) * 100
impar = impar / len(lista) * 100
print()
print(par)
print(impar)

# imprima listas diferentes para cada par e impar

import random
lista = []
par = []
impar = []
for i in range(5):
    lista.append(random.randint(1,10))
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
        
print(impar)
print(par)