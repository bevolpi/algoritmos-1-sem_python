#a)
qtde_bike = int(input("Insira a quantidade de bicicletas disponíveis: "))
preco = float(input("Insira o preço de cada aluguel diário: "))

fat_anual = ((((qtde_bike * 1/3) * preco) * 30)) * 12

print(f"O faturamento anual da empresa é de R$ {fat_anual:.2f}")

#b)
multa_cada = preco * 0.1
multa_mes = multa_cada * (((qtde_bike * 1/3) * 30) * 1/10)

print(f"O faturamento mensal adicional das multas é de R$ {multa_mes:.2f}")