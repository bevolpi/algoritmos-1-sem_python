'''Escreva um programa em python que leia um número na base binária e, em seguida, faça a sua
conversão para a base decimal. Antes de fazer a conversão, seu programa deverá validar se o
número informado realmente está na base de numeração binária. Se não estiver, não poderá ser
convertido'''

binario = input("Digite um número na base binária: ")
decimal = 0 
i = 0

valido = True
for digito in binario:
    if digito != '0' and digito != '1':
        valido = False
        break

if valido:
    binario = int(binario)
    while binario > 0:
        digito = binario % 10 #assim a gnt pega o último! -> 0
        decimal = decimal + digito * (2**i) # decimal = 0 + 0 * 2^0 
        i += 1 
        binario = binario // 10
        
print(decimal)