'''Escreva um programa em Python que leia um valor inteiro e positivo. O seu programa deverá
exibir um padrão triangular de números conforme exemplo mostrado na figura a seguir.
Suponha que na entrada de dados o usuário da aplicação tenha informado o número inteiro
4.'''

nm = int(input("Insira um nm inteiro e positivo: "))

if nm <= 0:
    print("Nm deve ser MAIOR que 0")
else:
    for linha in range(1, nm+1): # ou range(nm) -> pq não importa se é de 0 a 3 ou de 1 a 4
        for coluna in range(1, linha+1): # aqui só pode ser assim
# quando "linha" valer 1, vai imprimir "1", se for 2, imprime "1 2"
           print(coluna, end= ' ') #sem o end fica na vertical, com ele, fica na horiz
# ent precisa indicar que precisa dar um enter, com isso, damos um print em branco
        print( )

