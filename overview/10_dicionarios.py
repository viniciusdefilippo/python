# Dicionários
contatos = {
    'Pedro': '1234-5678',
    'Carlos': '9999-9999',
    'Beatriz': '8765-4321',
    'Marina': '8877-7788',
    'Eduardo': '9999-4545'
    }

print('\nImprimindo as chaves da lista:')
print(contatos.keys())

# Adicionando valores
contatos['Fernanda'] = '8888-1515'

print('\nImprimindo os valores da lista:')
print(contatos.values())

# Removendo valores
del contatos['Pedro']

print('\nImprimindo todos os itens da lista:')
print(contatos.items())

# Atualizando valores
contatos.update({'Carlos': '9999-8888', 'Marina': '8888-7777'})

print('\nImprimindo e manipulando as chaves e valores da lista:')
for (nome, telefone) in contatos.items():
    print(f'{nome}: {telefone}')

print('\nPesquisando valores no dicionário')
print('Por chave:')
print(contatos.__contains__('Carlos'))
print(contatos['Eduardo'])
print('Por valor:')
print('9999-4545' in contatos.values())
