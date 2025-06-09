'''Escreva um programa em Python para calcular e exibir no vídeo o valor da expressão: 
y = 1/1 - 1/2 + 1/3 ... +- 1/n'''

n = int(input("Informe o valor de n maior que zero: "))
y = 0
sinal = 1

if n <= 0:
    print("Valor de n deve ser MAIOR que zero: ")
else:
    for denominador in range(1, n+1):
        y = y + 1/denominador * sinal
        sinal *= -1
    print(f"y = {y}")
