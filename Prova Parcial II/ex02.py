'''Dizemos que um número de 4 dígitos é raro se a soma de seus dois primeiros dígitos for igual à soma de
seus dois últimos dígitos. Escreva um programa em Python que leia dois números inteiros de 4 dígitos(caso
os valores estejam fora do intervalo o programa deverá solicitar novos valores até que a entrada esteja
correta) representando o início e o fim de um intervalo de valores, por exemplo 1000 e 3000. O seu
programa deverá processar todos os números inteiros no intervalo e imprimir no terminal:
a) quantidade de números raros presentes no intervalo (levar em consideração o início e o fim do
intervalo). Exemplos de números raros: 3416 e 6134. Exemplos de números não raros: 4312 e 2055.
b) quantidade de números raros par e ímpar no intervalo especificado.'''

inicio = int(input("Digite o início do intervalo (4 dígitos): "))
fim = int(input("Digite o fim do intervalo (4 dígitos): "))

while inicio < 1000 or inicio > 9999 or fim < 1000 or fim > 9999:
    inicio = int(input("Início deve ter 4 dígitos! Digite novamente: "))
    fim = int(input("Fim deve ter 4 dígitos! Digite novamente: "))

qtde_raros = 0
qtde_raros_par = 0
qtde_raros_impar = 0

for i in range(inicio, fim + 1):
    nm = i
    soma_1 = 0
    soma_2 = 0
    for j in range(1, 5):
        digito = i % 10
        if j <= 2:
            soma_1 = soma_1 + digito
        if j >= 3:
            soma_2 = soma_2 + digito
        i = i // 10
    if soma_1 == soma_2:
        print(f"{nm} é um número raro")
        qtde_raros += 1
        if nm % 2 == 0:
            qtde_raros_par += 1
        else:
            qtde_raros_impar += 1
print(f"A quantidade de números raros entre {inicio} e {fim} é {qtde_raros}")
print(f"A quantidade de números raros pares é {qtde_raros_par}")
print(f"A quantidade de números raros ímpares é {qtde_raros_impar}")

