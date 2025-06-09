'''Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1. Windows Server
2. Unix
3. Linux
4. Netware
5. MacOS
6. Outro
Você foi contratado para desenvolver um programa em Python para ler a resposta de cada um dos
entrevistados na enquete e, ao final, exibir no terminal o resultado da enquete em porcentagem. O programa
deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos
valores além dos válidos para o programa (0 a 6).
Após os dados terem sido completamente informados, o programa deverá calcular a porcentagem de cada um
dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional Votos %
------------------- ----- ------
Windows Server 1500 17,04%
Unix 3500 39,77%
Linux 3000 34,09%
Netware 500 5,68%
Mac OS 150 1,71%
Outro 150 1,71%
------------------- -----
Total 8800
O Sistema Operacional mais votado foi o Unix, com 3500 votos,
correspondendo a 39,77% dos votos. Caso haja empate, o programa deverá
informar quem está empatada e qual a porcentagem. '''

print("Qual o melhor Sistema Operacional para uso em servidores?")
print("1 - Windows Server")
print("2 - Unix")
print("3 - Linux")
print("4 - Netware")
print("5 - Mac OS")
print("6 - Outro")
print("0 - Para sair")

windowsS = 0
unix = 0
linux = 0
netware = 0
macOS = 0
outro = 0

while True:
    resp = int(input("Resposta: "))
    if resp == 0:
        break
    if resp == 1:
        windowsS += 1
    elif resp == 2:
        unix += 1
    elif resp == 3:
        linux += 1
    elif resp == 4:
        netware += 1
    elif resp == 5:
        macOS += 1
    elif resp == 6:
        outro += 1
    else:
        print("Número inválido! Digite de 1 a 6 para continuar ou 0 para encerrar.")

total = windowsS + unix + linux + netware + macOS + outro

print("\nSistema Operacional   Votos   %")
print("-------------------  -----  ------")
if total > 0:
    print("Windows Server        ", windowsS, " ", round(windowsS/total*100, 2), "%")
    print("Unix                  ", unix, " ", round(unix/total*100, 2), "%")
    print("Linux                 ", linux, " ", round(linux/total*100, 2), "%")
    print("Netware               ", netware, " ", round(netware/total*100, 2), "%")
    print("Mac OS                ", macOS, " ", round(macOS/total*100, 2), "%")
    print("Outro                 ", outro, " ", round(outro/total*100, 2), "%")
else:
    print("Windows Server           0    0.00%")
    print("Unix                     0    0.00%")
    print("Linux                    0    0.00%")
    print("Netware                  0    0.00%")
    print("Mac OS                   0    0.00%")
    print("Outro                    0    0.00%")

print("Total                 ", total)

maior = windowsS
nome = "Windows Server"
if unix > maior:
    maior = unix
    nome = "Unix"
elif unix == maior and maior > 0:
    nome += " e Unix"
if linux > maior:
    maior = linux
    nome = "Linux"
elif linux == maior and maior > 0:
    nome += " e Linux"
if netware > maior:
    maior = netware
    nome = "Netware"
elif netware == maior and maior > 0:
    nome += " e Netware"
if macOS > maior:
    maior = macOS
    nome = "Mac OS"
elif macOS == maior and maior > 0:
    nome += " e Mac OS"
if outro > maior:
    maior = outro
    nome = "Outro"
elif outro == maior and maior > 0:
    nome += " e Outro"

if maior > 0:
    percentual = maior / total * 100
    if " e " in nome:
        print(f"O Sistema Operacional mais votado foi {nome}, cada um com {maior} votos, correspondendo, cada um, a {percentual:.2f}% dos votos.")
    else:
        print(f"O Sistema Operacional mais votado foi o {nome}, com {maior} votos, correspondendo a {percentual:.2f}% dos votos.")
else:
    print("0 respostas.")
