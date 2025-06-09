'''O seu programa deverá ler pelo terminal, um valor na base binária.
O seu programa deverá converter o valor lido para a base decimal.'''


binario = int(input("Insira o número em binário: ")) #100
decimal = 0
i = 0
resultado = binario # só p guardar e escrever a resp bonitiha

while binario > 0:
    digito = binario % 10 #assim a gnt pega o último! -> 0
    decimal = decimal + digito * (2**i) # decimal = 0 + 0 * 2^0 
    i += 1 
    binario = binario // 10

print(f"{resultado} --> {decimal}")