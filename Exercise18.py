somatorio = 0
superior = int(input('Digite um valor: '))
for i in range(superior + 1):
    print(2**i)
    somatorio += 2**i
print('O somatório é: ', somatorio)
