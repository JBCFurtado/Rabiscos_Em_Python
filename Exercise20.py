#Calcular o somatório dos n primeiros números.
soma = 0
limite_sup = int(input('Entre com o limite superior: '))
for i in range(1, limite_sup + 101):
    soma += i
print(soma)
