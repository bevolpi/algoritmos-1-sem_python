salario = int(input("Digite o salário mínimo: "))
quilowatts = float(input("Quantos quilowatts são utilizados em sua residência? "))

valorkw = (1/7 * salario) / 100
valorR = valorkw * quilowatts
valordesconto10 = 10/100 * valorR

# o valor em reais de cada quilowatt;
print(F"O valor em reais de cada quilowatt é: R${valorkw:.4}") 

# o valor em reais a ser pago pela residência;
print (f"O valor a ser pago é: R${valorR:.2}")

# o novo valor a ser pago pela residência considerando um desconto de 10%.
print (f"O valor a ser pago com 10% de desconto é: R${valordesconto10:.2f}")