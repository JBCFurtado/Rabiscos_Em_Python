# #FUNÇÃO SOMATORIA
# def somatorio(n):
#     soma = 0
#     for i in range(n+1):
#         soma += i
#     return soma
# b = int(input('Digite um valor: '))
# total = somatorio(b)
# print('O valor dos {0} números é {1}'.format(b, total))
##Exercicio 1
def somatorio():
    a = 0
    n = int(input('Digite o numero:'))
    for i in range(n + 1):
        a += i
    return(a)
print('Soma dos numeros =',somatorio())
