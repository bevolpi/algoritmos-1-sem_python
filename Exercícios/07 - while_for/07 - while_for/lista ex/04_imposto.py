'''Calcule e imprima no vídeo o valor do imposto de renda mensal que um grupo de n contribuintes
deverá pagar a partir da renda mensal e do número de dependentes (os dados dos contribuintes
deverão ser fornecidos via teclado e armazenados). Para cada contribuinte será feito um
desconto de 5% do salário mínimo vigente por dependente. Os valores da alíquota (porcentagem)
para o cálculo do imposto de renda são:
Renda mensal (R$) Alíquota (%)
Até 2 salários mínimos isento
2 a 3 salários mínimos 5
3 a 5 salários mínimos 10
5 a 7 salários mínimos 15
Acima de 7 salários
mínimos
20
Observe que deve ser fornecido o valor atual do salário mínimo para que o algoritmo calcule os
valores corretamente. Observação: a alíquota é a porcentagem que deverá ser descontada da
renda mensal.'''

sal_min = float(input(f"valor atual do salário min: R$ "))
n = int(input("número de contribuintes: "))
cont = 1

while cont <= n:
    renda = float(input(f"renda mensal de {cont}: R$"))
    dependentes = int(input(f"nm de dependentes de {cont}: "))
    desc_renda = (sal_min * 0.05) * dependentes
    renda_liquida = renda - desc_renda
    renda_salarios = renda_liquida / sal_min

    if renda_salarios <= 2:
        imposto = "isento"
    elif renda_salarios <= 3:
        imposto = renda_liquida * 0.05
    elif renda_salarios <= 5:
        imposto = renda_liquida * 0.10
    elif renda_salarios <= 7:
        imposto = renda_liquida * 0.15
    else:
        imposto = renda_liquida * 0.20
        
    print(f"Imposto de renda do contribuinte {cont}: R$ {imposto:.2f}")
    cont += 1