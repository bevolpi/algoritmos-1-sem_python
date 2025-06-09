'''Uma quitanda está vendendo frutas com a seguinte tabela de preços:
Se o cliente comprar mais de 8 kgs em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um programa em Python para
ler a quantidade (em kgs) de morangos, a quantidade (em kgs) de maças e a quantidade (em
kgs) de banana adquiridas e imprima no vídeo o valor a ser pago pelo cliente. '''

morango = float(input("Quantidade de morangos (kg): "))
maca = float(input("Quantidade de maçãs (kg): "))
banana = float(input("Quantidade de bananas (kg): "))

#COMO FAZ COM MATCH

if morango < 5:
    pc_morango = morango * 2.5
else:
    pc_morango = morango * 2.2
if maca < 5:
    pc_maca = maca * 1.8
else:
    pc_maca = maca * 1.5
if banana < 5:
    pc_banana = banana * 1
else:
    pc_banana = banana * 0.87
    
tt_kg = morango + maca + banana
tt_preco = pc_morango + pc_maca + pc_banana

if tt_kg > 8 or tt_preco > 25:
    tt_preco = tt_preco * 0.9

print(f"R: R$ {tt_preco}")
     
