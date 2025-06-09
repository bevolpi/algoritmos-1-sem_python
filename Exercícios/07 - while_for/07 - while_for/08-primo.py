'''Escreva um programa em Python que leia um valor inteiro e positivo. Imprima uma
mensagem no vídeo informando se o número digitado é ou não um número primo. Um
número é primo quando é divisível apenas por 1 e por ele mesmo.'''

nm = int(input("Insira um número inteiro e positivo: "))
tt_div = 0

if nm <= 0:
    print("Valor deve ser int e positivo")
else:
    for divisor in range(1, nm + 1):
        if nm % divisor == 0:
            tt_div += 1
    if tt_div == 2:
        print(f"{nm} é primo")
    else:
        print(f"{nm} não é primo")
        


'''if nm <= 0:
    print("Valor deve ser int e positivo")
else:
    if nm % 2 != 0 and nm % 3 != 0 and (nm == 2 or nm == 3):
        # print(f"{nm} é primo") -> NÃO PODE pq se nao fica repetindo
        resp = nm, "é primo"
    else:
        # print(f"{nm} não é primo")
        resp = nm, "não é primo"
print(resp) -> SEM O FOR'''