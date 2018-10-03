num = int(input('Entre com um número para saber a tabuada: '))
var = 1
print('Tabuada de {}'.format(num))
while(var <= 10):
    print('{0} X {1} = {2}'.format(var, num, (var * num)))
    var = var + 1
