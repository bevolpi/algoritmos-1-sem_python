# FATORIAL
# se quiser somar {1+1+1+1+1....+1}(100 vezes)?

'''
total = 0    (a cada execução é o valor q ta na total + 1) -> isso cria um acumulador
             (uma variável contadora controla o laço de repetição)
contador = 1
while contador <= 100:
    total = total + 1
    contador = contador + 1
print(total)'''

# se quiser somar {1+2+3+4+5+6+7+8+9+10}
'''
cont = 1
total = 0
while cont <=10:
    total = total + cont
    cont = cont + 1
print(total)'''

# se quiser {1*2*3*4*5*6*7*8*9*10}
'''
cont = 1
total = 1
while cont <=10:
    total = total * cont
    cont = cont + 1
print(total)'''

# se quiser {1+1/2+1/3+1/4+1/5...+1/10}

'''
cont = 1
total = 0
while cont <=10:
    total = total + 1/cont
    cont = cont + 1
print(total)
'''

# PORTANTO......... EX4
'''Escreva um programa em Python que calcule o fatorial de um número inteiro e positivo'''

nm = int(input("Insira um número inteiro: "))
cont = 1
total = 1
while cont <= nm:
    total = total * cont
    cont = cont + 1
print(f"{nm}! = {total}")

# ou
fat = 1
v1 = int(input("v1="))
if v1 <= 0:
    print("POSITIVO")
else:
    for cont in range(1, v1+1):
        fat = fat * cont
        cont += 1
    print(fat)

#EX 5
'''Escreva um programa em Python que calcule o valor da expressão: y = {1 + 1/2 + 1/3 ... 1/n}'''
nm = int(input("Insira um número inteiro: "))
cont = 1
total = 0

if nm <= 0:
    print("Valor de n deve ser MAIOR q 0")
else:
    while cont <= nm:
        total = total + 1/cont
        cont = cont + 1
    print(f"y = {total}")