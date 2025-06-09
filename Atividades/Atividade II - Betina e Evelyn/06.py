valor = int(input("Digite um número inteiro e positivo: "))
cont = 1
total = 1
soma = 0

while cont <= valor:
    total = total * cont
    cont = cont + 1

resultado = total
aux = resultado

while aux > 0:
    digito = aux % 10
    soma = soma + digito
    aux = aux // 10
    
print(f"{valor}! = {resultado}")
print(f"{resultado} --> {soma}")
