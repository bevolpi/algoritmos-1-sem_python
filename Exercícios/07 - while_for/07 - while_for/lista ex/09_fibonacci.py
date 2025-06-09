'''Escreva um programa em python que calcule e imprima no terminal o valor armazenado na série
de Fibonacci a partir da sua posição fornecida via teclado. Por exemplo, o número 8 está
armazenado na 7ª posição da série.'''

posicao = int(input("Escolha a posição na série de Fibonacci: "))

# Considerando a 1ª posição como 0
if posicao <= 0:
    print("A posição deve ser maior ou igual a 1.")
else:
    a = 0
    b = 1
    cont = 1
    while cont < posicao:
        temp = a + b
        a = b
        b = temp
        cont += 1
    print(f"O valor na posição {posicao} da série de Fibonacci é: {a}")
