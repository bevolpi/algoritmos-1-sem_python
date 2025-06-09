'''Escreva um programa em python para preencher um vetor de 1000 posições
com valores fornecidos pelo usuário. Imprima no vídeo apenas os números
primos armazenados no vetor. Um número é primo quando ele tem apenas 2
divisores (1 e ele mesmo)'''

lista = []
primos = []
for i in range(5):
    lista.append(int(input("Insira: "))) 
    tt_div = 0
    for j in range(1, lista[i] + 1):
        if lista[i] % j == 0:
            tt_div += 1
    if tt_div == 2:
        primos.append(lista[i])

print(primos)