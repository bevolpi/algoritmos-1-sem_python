"""A delegacia de polícia da pequena cidade de Springfield conta com somente 3 policiais: o chefe
de polícia Clancy, e os policiais Eddie e Lou. Como é de se esperar, esse pequeno contingente de
policiais não consegue atender imediatamente a todos os chamados policiais. Portanto, você foi
contratado para criar um sistema de atendimento (um programa escrito em linguagem de
programação python), de maneira que cada um dos policiais fique com um conjunto equilibrado
de chamados.
Considere os requisitos:
a) Cada ocorrência deve ser de um tipo: Direção Perigosa, Barulho, Bebedeira, Homer.
b) Cada ocorrência deve ser de um nível de gravidade: Baixo, Médio, Alto.
c) Toda ocorrência do tipo Homer tem nível de gravidade alto.
d) Novas ocorrências devem ser atribuídas ao policial com menos ocorrências;
e) Ocorrências do tipo Homer sempre são atribuídas ao chefe de polícia.
A cada registro de ocorrência o sistema deve imprimir um resumo da quantidade de ocorrências
de cada policial, o número de ocorrências do tipo Homer e o percentual de ocorrências do tipo
“Direção Perigosa” em relação do total de ocorrências cadastradas."""



clancy = 0
eddie = 0
lou = 0
homer_count = 0
direcao_perigosa_count = 0
total = 0

while True:
    print("\nTipos de ocorrência:")
    print("1 - Direção Perigosa")
    print("2 - Barulho")
    print("3 - Bebedeira")
    print("4 - Homer")
    tipo = int(input("Escolha o tipo de ocorrência (1-4, 0 para sair): "))
    if tipo == 0:
        break
    if tipo < 1 or tipo > 4:
        print("Tipo inválido.")
        continue

    if tipo == 4:
        gravidade = 3  # Homer sempre é alto
    else:
        print("Níveis de gravidade:")
        print("1 - Baixo")
        print("2 - Médio")
        print("3 - Alto")
        gravidade = int(input("Escolha o nível de gravidade (1-3): "))
        if gravidade < 1 or gravidade > 3:
            print("Gravidade inválida.")
            continue

    # Atribuição do policial
    if tipo == 4:
        clancy += 1
        homer_count += 1
    else:
        # Atribui ao policial com menos ocorrências
        if clancy <= eddie and clancy <= lou:
            clancy += 1
        elif eddie <= lou:
            eddie += 1
        else:
            lou += 1

    if tipo == 1:
        direcao_perigosa_count += 1

    total += 1

    # Resumo
    print("\nResumo:")
    print("Clancy:", clancy, "ocorrência(s)")
    print("Eddie:", eddie, "ocorrência(s)")
    print("Lou:", lou, "ocorrência(s)")
    print("Ocorrências do tipo Homer:", homer_count)
    if total > 0:
        perc = (direcao_perigosa_count / total) * 100
    else:
        perc = 0
    print("Percentual de 'Direção Perigosa': %.2f%%" % perc)