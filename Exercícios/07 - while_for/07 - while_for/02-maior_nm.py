''' imprimir o maior numero de 5 numeros q o usuario deu'''
maior = 0
cont = 1
while cont <= 5:
    v1 = int(input("v1="))
    if maior == 0 or v1 > maior:
        maior = v1
    cont += 1
print(maior)
# ouuu 

contador = 1
maior = float('-inf')
while contador <= 5:
    nms = int(input("Insira os números: "))
    if nms > maior:
        maior = nms
    contador = contador + 1 
print(maior)