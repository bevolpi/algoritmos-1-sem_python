'''No último final de semana foi realizado um campeonato de arco e flecha na faculdade. Durante
a competição, cada competidor poderia lançar duas vezes a flecha ao alvo e a distância de cada
lançamento para cada jogador era registrada pelos juízes da competição. O competidor vencedor
foi aquele que lançou a flecha mais próxima do alvo nas duas tentativas, ou seja, o vencedor
atingiu a menor distância nas duas tentativas.
Escreva um programa em python que leia o nome e a distância atingida por cada competidor nas
duas tentativas. O seu programa deverá imprimir no terminal o nome do vencedor.'''

qtde = int(input("Insira a qtde de competidores: "))

menor1 = float('+inf')
menor2 = float('+inf')
vencedor = ""

for i in range(qtde):
    nome = input(f"Nome do competidor {i+1}: ")
    v1 = float(input("Distância do 1º lançamento: "))
    v2 = float(input("Distância do 2º lançamento: "))

    if v1 < menor1 and v2 < menor2:
        menor1 = v1
        menor2 = v2
        vencedor = nome
    if v1 < menor1 and v2 > menor2:
        vencedor = "ninguém"
        menor1 = v1
        menor2 = v2 
    if v1 > menor1 and v2 < menor2:
        vencedor = "ninguém"
        menor1 = v1
        menor2 = v2         

if vencedor == "ninguém":
    print("Nenhum competidor conseguiu ser melhor nas duas tentativas.")
else:
    print("Vencedor:", vencedor)