'''Cada novo termo na sequência de Fibonacci é gerado pela adição dos dois termos anteriores.
Começando com 1 e 2, os 10 primeiros termos são: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Considerando os termos da sequência de Fibonacci cujos valores não excedem quatro milhões,
escreva um programa em python que calcule e imprima no terminal a soma de todos os termos
de valor par'''

a = 0
b = 1
temp = 0
soma = 0
for posicao in range(1, 35):
    temp = a + b
    a = b
    b = temp
    if temp % 2 == 0:
        soma = soma + temp
print(soma)