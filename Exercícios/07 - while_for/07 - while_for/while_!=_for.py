# x = x + 1 -> x += 1 -> x++
# y = y - 3 -> y -= 3
# a = a * x -> a *= x
# b = b / t -> b /= t
# c = c % z -> c %= z

cont = 0 #1
while cont <= 5: #2
    print(cont)
    cont += 1 #3
print("------------------------")
print(cont)

print("___________________________________________")
# no for, as 3 linhas são em 1 só
for cont in range(6):
    print(cont)
print("------------------------")
print(cont)