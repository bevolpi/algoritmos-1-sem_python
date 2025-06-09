'''Um número é chamado de palíndromo se tem a mesma leitura nos dois sentidos, por exemplo, o
número 212 (da direita para esquerda ou da esquerda para a direita é o mesmo número). O maior
número palíndromo gerado pelo produto de dois números naturais com dois dígitos é 9009 (91 x
99). Escreva um programa em python que encontre o maior número palíndromo formado pela
multiplicação de dois números naturais com três dígitos.'''

maior_palindromo = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        produto = i * j
        if str(produto) == str(produto)[::-1]:
            if produto > maior_palindromo:
                maior_palindromo = produto

print(maior_palindromo)

#OUUU

maior = 1
inicio = 100
fim = 1000

for i in range(inicio, fim):
    for j in range(inicio, fim):
        produto = str(i * j)
        tam = len(produto)
        ehPalindromo = True
        
    for k in range(0, int(tam/2)):
        if(produto[k] != produto[tam-k-1]):
            ehPalindromo = False
            
    if ehPalindromo:
        if(maior < int(produto)):
            maior = int(produto)
            
print(maior)
            