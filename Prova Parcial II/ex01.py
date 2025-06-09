'''O país A tem cerca de pA mil habitantes, enquanto o país B tem aproximadamente pB mil habitantes.
O país A tem uma taxa de crescimento anual de tA, enquanto o país B cresce à taxa de tB. 
Suponha que a população do país A é menor que a do país B, mas a taxa de crescimento de A é maior 
que a taxa de crescimento de B. Escreva um programa em Python que leia (pelo terminal) os 
dados dos dois países e imprima no terminal quantos anos são necessários para que a população 
do país A ultrapasse a população do país B em número de habitantes.'''

pA = int(input("Insira a quantidade de habitantes do país A: "))
pB = int(input("Insira a quantidade de habitantes do país B: "))
tA = float(input("Insira a taxa de crescimento anual do país A (em %): "))
tB = float(input("Insira a taxa de crescimento anual do país B (em %): "))

anos = 0
while pA <= pB:
    pA = int(pA * (1 + tA / 100))
    pB = int(pB * (1 + tB / 100))
    anos += 1

print(f"A quantidade de anos necessária para pA ultrapassar pB = {anos}")