'''Escreva um programa em Python que imprima no terminal a soma dos números ímpares em um
intervalo. O início e o fim do intervalo deverão ser fornecidos pelo usuário da aplicação. A soma
deve englobar os extremos do intervalo'''

v1 = int(input("v1="))
v2 = int(input("v2="))
soma = 0
for i in range(v1, v2 + 1):
    if i == v1 or i == v2 or i % 2 != 0:
        soma = soma + i
print(soma)