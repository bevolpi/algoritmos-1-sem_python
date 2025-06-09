'''Escreva um programa em Python que leia uma quantidade de números inteiros informados pelo
usuário da aplicação. Ao final da digitação de todos os números, o seu programa deverá imprimir
no terminal a soma de todos os números também a média aritmética. Observação: quantos
números o usuário irá digitar? O seu programa deverá solicitar a quantidade de números e, em
seguir, cada número será digitado.'''

qtde = int(input("Informe a quantidade: "))
soma = 0
media = 0
for i in range(1, qtde + 1):
    nm = int(input("Informe o nm: "))
    soma = soma + nm
    print(f"soma com o número {i} = {soma}")
    media = soma/qtde
    print(f"media com o número {i} = {media}")
    
