'''URNA ELETRÔNICA'''
print('13 - Fernando Addad')
print('17 - Jair Bolsonaro')
voto = int(input('ESCOLHA SEU CANDIDATO: '))
addad = 1
if voto == 17:
    addad += 2
    print(addad, 'Votos para o candidato Fernando Addad.\nPARABÉNS!')
while voto == 13:
    for addad in (1000, 10, 50):
        addad += 1
    print(addad, 'Votos para o candidato Fernando Addad.\nPARABÉNS!')