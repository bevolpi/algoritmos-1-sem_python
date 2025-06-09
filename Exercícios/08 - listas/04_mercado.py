'''Escreva um programa em python que leia o nome de cada produto
comercializado por um vendedor, a respectiva quantidade em estoque e o valor
unitário (todos esses valores devem ser armazenados). O seu programa deverá:
a) Imprimir o nome do produto mais caro (considerar mais de um produto com o mesmo valor).
b) Imprimir o valor total (em reais) de cada produto armazenado.
c) Imprimir o valor total (em reais) armazenado em estoque.'''

qtde = int(input("Qtde de produtos: "))
nome = []
estoque = []
valor = []

for i in range(qtde):
    print(f"-------Produto {i+1}-------")
    nome.append(input(f"Insira o nome do produto {i+1}: "))
    estoque.append(int(input(f"Insira a quantidade do produto {i+1} no estoque: ")))
    valor.append(float(input(f"Insira o valor do produto {i+1}: ")))
    
# a)
print()
maior_valor = max(valor)
print("\nProduto(s) mais caro(s):")
for i in range(len(valor)):
    if valor[i] == maior_valor:
        print(f"- {nome[i]} = R$ {valor[i]:.2f}")
        
# b)
soma_tt = 0
print("\nValor total de cada produto: ")
for i in range(qtde):
    soma_vl_cada = valor[i] * estoque[i]
    print(f"- {nome[i]} = R$ {soma_vl_cada:.2f}")
# c)
    soma_tt += soma_vl_cada
print(f"\nValor total no estoque: R$ {soma_tt:.2f}")













# nm = int(input("Insira o número de produtos necessários: "))
# nome = []
# qtde = []
# valor = []
# caro = 0

# for i in range(nm + 1):
#     nome.append(input("Nome do produto: "))
#     qtde.append(int(input("Quantidade em estoque: ")))
#     valor.append(float(input("Valor unitário: ")))
#     print("-------")
#     if i == 0 or valor[i] > caro:
#         caro = valor[i]
#     tt_valor_prod = valor[i] * qtde[i]
#     tt_valor = tt_valor_prod * nm
        
# print(caro)
# print(nome)
# print(qtde)
    
    