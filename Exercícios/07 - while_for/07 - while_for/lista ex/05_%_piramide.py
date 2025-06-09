'''Escreva um programa em Python que leia um valor inteiro n que representa o número de linhas
que serão impressas no vídeo. O seu programa deverá imprimir um triângulo formado por
asteriscos (%) conforme figura a seguir. O número de linhas de impressão será exatamente o valor
de n informado pelo usuário da aplicação. Por exemplo, suponha que o usuário tenha informado
o valor 6 para n, o triângulo deverá ter o seguinte formato
2
%
%%
%%%
%%%%
%%%%%
%%%%%%'''

linhas = int(input("insira nm de linhas: "))
for i in range(1, linhas+1):
    for j in range(i):
        print("%", end= "")
    print()