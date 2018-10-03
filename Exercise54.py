#COPIA DE LISTA
print('Cópia de listas')
l = [1, 2, 3, 4, 5]
v = l
print(v)
x = [2, 8, 9]
z = x[:]
print('x = ', x)
print('z = ', z)
z.append(45)
x.append(87)
print('x = ', x)
print('z = ', z)

