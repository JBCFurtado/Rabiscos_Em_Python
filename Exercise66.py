# #Acrescente zero no inicio da lista
# lista = [1, 2, 10, 5, 20]
# valor = 10
# resultado = valor in lista
# print(resultado)

lista9 = [2, 4, 6, 8, 12]
valor = 10
resultado = False
for i in range(len(lista9)):
    if lista9[i] == valor:
        resultado = True
    else:
        resultado = False
print(resultado)
