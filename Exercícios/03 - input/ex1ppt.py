# entrada de dados
altura = float(input("Digite a altura em cm: "))
base = float(input("Digite a base em cm: "))

# processamento 
area = base * altura
perimetro = (base * 2) + (altura * 2)

# saída
print(f"O resultado da área é: {area:.2f}")
print(f"O resulta do perímetro é: {perimetro:.2f}")