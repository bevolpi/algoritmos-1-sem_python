'''. Escreva um programa em Python que leia n pontos no plano cartesiano (coordenada x e coordenada y) e
imprima no vídeo as coordenadas (x e y) do ponto mais distante e mais perto da origem (ponto de
coordenadas x = 0 e y = 0). A quantidade n de pontos deverá ser informada no início do programa. A
fórmula da distância entre dois pontos a e b é dada por:
d = sqrt(((xa - xb)**2) + ((ya - yb)**2))
Na fórmula apresenta, xa indica a coordenada x do ponto a e, xb indica a coordenada x do ponto b. A mesma
observação é feita para a coordenada y.
Observação: não serão levados em consideração empates, ou seja, dois ou mais pontos que tenham a
maior distância em relação a origem dos pontos. Seguem alguns valores de teste.
Qual a quantidade de pontos que serão informados? --> 4
Ponto 1:
x --> 6
y --> 5
Distância até a origem --> 7,8102
Ponto 2:
x --> -9
y --> -3
Distância até a origem --> 9,4868
Ponto 3:
x --> -8
y --> -10
Distância até a origem --> 12,8062
Ponto 4:
x --> -4
y --> 4
Distância até a origem --> 5,6569
O ponto mais distante tem coordenadas --> (-8, -10)
O ponto mais perto tem coordenadas --> (-4, 4)'''

from math import sqrt

n = int(input("Qual a quantidade de pontos que serão informados? "))

d_maior = -1
d_menor = -1
x_max = 0
y_max = 0
x_min = 0
y_min = 0

for i in range(1, n + 1):
    print(f"Ponto {i}:")
    x = float(input("x --> "))
    y = float(input("y --> "))
    dist = sqrt(x**2 + y**2)
    print(f"Distância até a origem --> {dist:.4f}")
    if dist > d_maior or d_maior == -1:
        d_maior = dist
        x_max = x
        y_max = y
    if dist < d_menor or d_menor == -1:
        d_menor = dist
        x_min = x
        y_min = y

print(f"O ponto mais distante tem coordenadas --> ({x_max}, {y_max})")
print(f"O ponto mais perto tem coordenadas --> ({x_min}, {y_min})")