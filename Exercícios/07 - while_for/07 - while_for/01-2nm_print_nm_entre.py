'''Desenvolver um programa em Python que leia dois valores inteiros e positivos. O segundo valor
deverá ser maior do que o primeiro. O seu programa deverá imprimir todos os números inteiros entre
o primeiro e o segundo número digitado pelo usuário (inclusive os valores digitados pelo usuário).'''
v1 = int(input("v1="))
v2 = int(input("v2="))
cont = v1
while cont <= v2:
    print(cont)
    cont +=1
    
# ou

v1 = int(input("v1="))
v2 = int(input("v2="))
for cont in range(v1, v2+1):
    print(cont)