valorhoraaula = float(input("Digite o valor da hora-aula: R$"))
horasmes = float(input("Digite a quantidade de horas trabalhadas no mês: "))
descontoINSS = float(input("Digite a porcentagem de desconto do INSS: "))

'''a) calcula-se o valor do salário bruto (valor da hora-aula multiplicada pelo número
de horas trabalhadas).'''
salbruto = valorhoraaula * horasmes

'''b) A partir do salário bruto, calcula-se o valor que será descontado referente ao
INSS.'''
valordescontadoINSS = salbruto * (descontoINSS / 100)

'''#c) Calcula-se o salário líquido mensal (valor do salário bruto menos o valor do
desconto do INSS.'''
salliqmes = salbruto - valordescontadoINSS

# d) Exibir o valor do salário líquido com apenas duas casas decimais.
print(f"O valor do ssalário líquido é: {salliqmes:.2f}")