'''Escreva um programa em Python que leia um número inteiro. Imprimir seus divisores no vídeo
(considerar apenas o intervalo entre 0 e 10). O programa deve permitir reprocessamento, ou seja,
após a sua execução deverá ser perguntado ao usuário se ele deseja executar novamente ou finalizar a
aplicação.'''

while True:
    v1 = int(input("v1="))
    for cont in range(1, 11):
        if v1 % cont == 0:
            print(cont)
    repetir = int(input("quer repetir? sim 1 não 2 "))
    if repetir == 2:
        break