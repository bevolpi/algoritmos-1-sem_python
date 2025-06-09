# GUARDAR
# SEQUENCIA DE FIBONACCI EM LISTA:

v = [0] * 30
v[0], v[1] = 1, 1

for i in range(2, 28):
    v[i] = v[i - 1] + v[i - 2]
print(f"{v[12]}") #só p saber o valor no índice 12