'''Escreva um programa em python para preencher um vetor de 1000 posições
com valores fornecidos pelo usuário. Imprima no vídeo apenas os números
primos armazenados no vetor. Um número é primo quando ele tem apenas 2
divisores (1 e ele mesmo)'''

from math import sqrt
lista = []

#preenchimento da lista com valores informados via teclado
for _ in range(6):
    lista.append(int(input("Insira: ")))
    
#impressão dos números primos armazenados
for numero in lista:
    tt = 0
    for i in range(2, int(sqrt(numero)+1)): #pode ser sqrt(lista[i]) ///// isso deixa + rápido!
#pegamos a raiz pq é regra: a qtde de divisores antes da raiz = a qtde depois!
        if numero % i == 0:
            tt += 1
            break # significa que se o nm nao foi divisível por nenhum i, ele é primo! por isso
                  # o break, assim quebra o código e o tt continua sendo 0
    if tt == 0:
        print(numero, end= " ")