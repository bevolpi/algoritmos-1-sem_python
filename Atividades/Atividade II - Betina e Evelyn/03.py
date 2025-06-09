qtde_alunos = int(input("Insira a quantidade de alunos pesquisados: "))
favor = 0
contra = 0
total = 0

for i in range(1, qtde_alunos + 1):
    resp = int(input("A favor (digite 1), contra (digite 2): "))
    if resp == 1:
        print(f"O aluno {i} é a favor.")
        favor += 1
        total += 1
    elif resp == 2:
        print(f"O aluno {i} é contra.")
        contra += 1
        total += 1
    else:
        print("Escolha inválida.")

perc_contra = contra * 100 / total
perc_favor = favor * 100 / total

print("\n----Resultados------")
print(f"        Quantidade   Percentual")
print(f"Favor        {favor}        {perc_favor}%")
print(f"Contra       {contra}        {perc_contra}%")
print("----------------------")
print(f"Total        {total}")
    