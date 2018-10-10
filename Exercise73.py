#Multiplo primeiro é multiplo do segundo
a = int(input('Digite'))
b = int(input('Digite'))
def multiplo(a, b):
    if a % b == 0:
        return(True)
    else:
        return(False)
print(multiplo(a, b))
