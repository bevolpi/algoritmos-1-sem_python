'''Faça um programa em Python que leia um número inteiro e positivo e imprima todos os
seus divisores (positivos e negativos)'''

# A MELHOR: 
nm = int(input("Insira um número inteiro e positivo: "))

if nm <= 0:
    print("Valor deve ser int e positivo")
else:
    for cont in range(nm * -1, nm + 1): #ou (-nm, nm + 1)
        if cont != 0 and nm % cont == 0:
            print(f"{cont}")
            
#OU
if nm <= 0:
    print("Valor deve ser int e positivo")
else:
    for cont in range(nm * -1, nm + 1): #ou (-nm, nm + 1)
        if cont == 0:
            cont = cont + 1
        elif nm % cont == 0:
            print(f"{cont}")
            

# OU
if nm <= 0:
    print("Valor deve ser int e positivo")
else:
    for cont in range(1,nm + 1): #começa em 1 pq é INT E POSIT
        if cont !=0 and nm % cont == 0:
            print(f"{cont}")
            print(f"{-cont}")
        cont += 1
        
