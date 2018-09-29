somatorio = 0
inferior = int(input('Valor inferior: '))
superior = int(input('Valor superior: '))
for i in range(inferior, superior + 1):
    somatorio += i
print(somatorio)
