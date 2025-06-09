'''Escreva um programa em Python que calcule e imprima no vídeo o valor total das
compras de um cliente. O valor total deverá ser calculado a partir da soma do preço de
cada produto. Em seguida o usuário deverá escolher a forma de pagamento:
À vista com 10% de desconto;
Em duas vezes com um acréscimo de 15.5%'''

qtde = int(input("Informe a quantidade de itens comprados: "))
valor = 0

for cont in range(qtde):
    preco = float(input("Insira o preço do produto (em reais): "))
    valor = valor + preco 
pag =  int(input("Insira 1 para pagamento à vista e 2 para pagamento em 2x: "))
if pag == 1:
    valor = valor * 0.9 
    print(f"R$ {valor:.2f}")
elif pag == 2:
    valor = valor * 1.155
    print(f"R$ {valor:.2f}")
else: 
    print("Valor inválido")
    
# ouu
qtde = int(input("Insira a qtde de produtos: "))
cont = 1
soma = 0
while cont <= qtde:
    valor = float(input(f"Insira o valor do produto {cont}: "))
    soma = soma + valor
    cont += 1
pag = int(input("Insira 1 à vista e 2 de 2x: "))
if pag == 1:
    soma = soma * 0.9
    print(f"R$ {soma:.2f}")
elif pag == 2:
    soma = soma * 1.155
    print(f"R$ {soma:.2f}")
else: 
    print("Valor inválido")