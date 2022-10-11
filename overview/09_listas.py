# Lista
# lista de inteiros
lista1 = [1, 2, 3]
# lista de Strings
lista2 = ['josé', 'maria']
# lista de vários tipos
lista3 = ['oi', 3.0, 40, True]
# insere 'pedro' na primeira posição da lista 2
lista2.insert(0, "pedro")
# remove 'josé' da lista 2
lista2.remove('josé')
# insere 'josé' na posição 2 da fila da lista 2
# lembrando que a fila começa na posição 0
lista2.insert(2, 'josé')

print('\nImprimindo toda lista:')
print(lista2)

print('\nImprimindo valores lista:')
for elemento in lista2:
    print(elemento)

print('\nImprimindo por índices:')
for i in range(0, len(lista2)):
    print(lista2[i])

