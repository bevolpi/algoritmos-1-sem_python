'''O fatorial de um número natural é representado por um ponto de exclamação (!), por exemplo,
10! = 10 x 9 x 8 x ... x 3 x 2 x 1 = 3628800. 
A soma dos dígitos do número 10! é 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. 
Escreva um programa em python que leia um valor natural informado pelo teclado e
calcule e imprima a soma de todos os dígitos do fatorial do número informado.'''


nm = int(input("Insira um número inteiro: "))
cont = 1
total = 1
while cont <= nm:
    total = total * cont
    cont = cont + 1
print(f"{nm}! = {total}")

decimal = 0
i = 0
resultado = total
soma = 0

while i <= len(str(resultado)):
    digito = total % 10 
    total = total // 10 
    soma = soma + digito
    i += 1
    
print(f"{resultado} --> {soma}")
