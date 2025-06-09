'''Escreva um programa em python que preencha um vetor com números inteiros (o
tamanho fica a seu critério). Em seguida seu programa deverá encontrar o ponto de
equilíbrio na lista. O ponto de equilíbrio é a posição na qual a soma dos números à
esquerda é igual a soma dos números à direita. Exemplo:
Entrada: lista = [1, 3, 5, 2, 2, 1, 6]
Saída: 3 (Índice onde os elementos à esquerda [1, 3, 5] somam 9 e os elementos à
direita [2, 1, 6] somam 9)'''

# Preenchendo a lista
lista = []
n = int(input("Quantos números deseja inserir? "))
if n % 2 == 0:
    print("A qtde precisa ser ímpar")
else:
    for i in range(n):
        valor = int(input(f"Digite o {i+1}º número: "))
        lista.append(valor)

    # Encontrando o ponto de equilíbrio
    ponto = -1
    for i in range(1, len(lista)):
        soma_esq = 0
        soma_dir = 0
        for j in range(i):
            soma_esq += lista[j]
        for j in range(i, len(lista)):
            soma_dir += lista[j]
        if soma_esq == soma_dir:
            ponto = i
            break

if ponto == -1:
    print("Não existe ponto de equilíbrio na lista.")
else:
    print(f"Ponto de equilíbrio encontrado no índice {ponto}.")