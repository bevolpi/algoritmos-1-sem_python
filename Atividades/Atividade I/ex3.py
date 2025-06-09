from math import ceil
h = float(input("Digite a altura do reservatório (em metros): "))
r = float(input("Digite o raio do reservatório (em metros): "))
custo = float(input("Digite o custo de cada unidade de isolamento: "))

area = 2 * 3.14 * r * (r + h)

uni = ceil(area / 2.85)

custo_final = custo * uni

print(f"Área total a ser isolada: {area:.2f}m²")
print(f"Quantidade de unidades de isolamento: {uni}") 
print(f"Custo total: R${custo_final:.2f}")
