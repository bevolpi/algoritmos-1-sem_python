'''Escreva um programa em python que leia um valor inteiro a partir do teclado. Imprima uma
mensagem informando para o usuário a quantidade de dígitos que compõe o valor informado.'''

n = int(input("v1="))

if n == 0:
    print("1 dígito")
elif n > 0:
    cont = 1
    while True:
        if n <= 10 ** cont:
            resposta = cont
            break
        cont += 1
    print(f"O nm tem {cont} dígitos")
    
    
    