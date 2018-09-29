valor = int(input('Digite um valor: '))
for i in range(1, 25):
        print('{0}x de R$ {1}'.format(i, valor // i))
