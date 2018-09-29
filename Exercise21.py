n = int(input('Entre com o limite superior: '))
somatorio = 0
for i in range(1, n + 1):
    somatorio += (2*i + 5*i)**2
print(somatorio)
