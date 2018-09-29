resultado = 0
a = int(input('Digite a: '))
b = int(input('Digite a: '))
n = int(input('Digite a: '))
for i in range(1, n+1):
    resultado += (a-b*i + i**2)
print(resultado)
