def media(lista):
    total = 0
    for i in lista:
        total += i
    return total/len(lista)
lista1 = [3,5,8,9]
lista2 = [3, 6, 9]


print(media(lista1))
print(media(lista2))