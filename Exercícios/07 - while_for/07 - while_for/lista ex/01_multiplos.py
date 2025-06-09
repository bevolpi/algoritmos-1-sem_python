'''Faça um programa em Python que determine o mostre os cinco primeiros múltiplos de 3, a partir
de um número inteiro informado via teclado pelo usuário da aplicação.'''

v1 = int(input("Digite um número inteiro: "))

contador = 0

while contador < 5:
    if v1 % 3 == 0:
        print(v1)
        contador += 1
    v1 += 1