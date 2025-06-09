nm = int(input("Insira valor inteiro: "))

fator = 2
maior = 1

while nm > 1:
    if nm % fator == 0:
        maior = fator
        nm //= fator
    else:
        fator += 1

print(f"O maior fator primo é {maior}")           