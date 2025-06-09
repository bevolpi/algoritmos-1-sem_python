'''Escreva um programa em Python que leia um número inteiro. Imprimir sua tabuada no vídeo
(considerar apenas o intervalo entre 0 e 10). O programa deve permitir reprocessamento, ou seja,
após a sua execução deverá ser perguntado ao usuário se ele deseja executar novamente ou finalizar a
aplicação.'''

tabuada = 1
repetir = "sim"
while repetir == "sim":
    nm = int(input("Insira núm inteiro: "))
    contador = 0
    while contador <= 10:
        tabuada = nm * contador
        print(tabuada)
        contador = contador + 1
    repetir = input("Quer repetir? (Sim ou Não) ")
    
# ou

print("---------")   
while True:
    v1 = int(input("v1="))
    for cont in range(0, 11):
        tabuada = v1 * cont
        print(tabuada, end= " ")
    print()
    repetir = int(input("quer repetir? sim 1 não 2 "))
    if repetir == 2:
        break
