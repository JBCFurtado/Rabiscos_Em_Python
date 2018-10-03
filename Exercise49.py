notas = [0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input('Digite as notas: '))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print('nota {0} = {1}'.format(x, notas[x]))
    x += 1
print("A Média é:  {0}".format(soma/x))
