'''Um comerciante deseja imprimir um relatório contendo a porcentagem de
aumento de cada produto comercializado em relação ao mesmo período do ano
passado. Você deverá escrever um programa em python para ler e armazenar o
nome do produto, o valor comercializado no ano passado e o valor
comercializado no momento. A saída do seu programa deverá ser o nome de
cada produto e a porcentagem de aumento. A quantidade de produto
comercializada deverá ser informada pelo comerciante.'''

nome = []
valor_antes = []
valor_agora = []
qtde = int(input("Insira a qtde de produtos: "))

def ler_dados():
    for i in range(qtde):
        print(f"---------Produto {i} ---------")
        nome.append(input(f"Digite o nome do produto {i}: "))
        valor_antes.append(float(input("Insira o valor do ano passado: ")))
        valor_agora.append(float(input("Insira o valor do momento: ")))
        
ler_dados()
print("----------Porcentagem de aumento--------")

def percentual():
    for i in range(qtde):
        porcentagem = (valor_agora[i] - valor_antes[i]) / valor_antes[i] * 100
        print(f"Produto {nome[i]} --> {porcentagem}% de aumento")
        
percentual()

        