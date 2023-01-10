# Dicionários são listas com posições textuais (estilo JSON)

# Lista:
lista = ['Everton', 29, 'São José']
print(lista)

# Dicionário equivalente:
dicio = {
    'nome': 'Everton',
    'idade': '29',
    'cidade': 'São José'
}

print(dicio)


# declarando dicionário vazio - 2 formas

dicionario2 = {}
dicionario3 = dict()
dicionario4 = {
    'nome': 'Teste',
    'idade': 300,
    'key3': True,
    'key4': [0,1]
}

print()

# keys sempre strings
# values pode ser qualquer tipo de dado

print(dicionario2)
print(dicionario3)
print(dicionario4)

print()

# Acessando os valores

print(dicio['nome'])
print(dicio['idade'])
print(dicio['cidade'])

print()

# Modificando valores

dicio['nome'] = 'Phelipe'
print(dicio)


print()

# Adicionando novas chaves

dicio['peso'] = 75
print(dicio)

print()
# Atenção na declaração das chaves - sensitive key

dicio['Cidade'] = 'São João'
print(dicio)


print()
# Deletando valor
del dicio['Cidade']
print(dicio)



dicio # dicionário completo
dicio.values() # somente os valores
dicio.keys() # somente as chaves
dicio.items() # chaves + valores do dicionário

print()
# Usando for com Dicionário, e imprimindo todos os valores

for v in dicio.values():
    print(f'o valor é {v}')
print()

for k in dicio.keys():
    print(f'A chave é {k}')
print()

for k,v in dicio.items():
    print(f'A chave é {k} e o valor é {v}')
print()

# Exercício 1

# declaração
cardapio = {
    'lanche': 10.9,
    'batata': 5.5,
    'refri': 3.9
}

# mostrar cardápio
print('-'*30)
print('-'*10, 'CARDÁPIO', '-'*10)
for k, v in cardapio.items():
    print(f'{k:.<22} R${v:5.2f}')
print('-'*30)
print()
# Perguntar qts itens ele quer
qtd = {}

for k in cardapio.keys():
    qtd[k] = int(input(f'Quantos {k} você quer? '))
print()

soma = 0
for v1, v2 in zip(cardapio.values(), qtd.values()):
    soma += (v1 * v2)

# Imprimindo recibo
print('-'*30)
for k, v in qtd.items():
    print(f'{v} {k:.<20} = R${v * cardapio[k]:5.2f}')
    
print('-'*30)
print(f'O valor total é de: R$ {soma:.2f}')

print()
print()

# Copiando a lista de dicionários

pessoas = [
    {'nome': 'Everton', 'idade':29, 'cidade':'São José'},
    {'nome': 'Phelipe', 'idade':26, 'cidade':'Nova Iguaçu'},
    {'nome': 'Teste', 'idade':22, 'cidade':'Madrid'}
]

# Cada lista
print(pessoas[2])

# Nome da pessoa 2
print(pessoas[1]['nome'])

# Idade da pessoa 1
print(pessoas[0]['idade'])

# Cidade da pessoa 3
print(pessoas[2]['cidade'])

print()
print()

for l in pessoas:
    print(l)
    for k, v in l.items():
        print(k,v)

print()
print()

# Imprimindo os valores estruturados

for i, p in enumerate(pessoas):
    for k, v in p.items():
        print(f"A pessoa {i+1} tem {p['idade']} anos, se chama {p['nome']} e mora em {p['cidade']}")


# Declarando lista de dicionários vazios

temp = {}
pessoas = []

while True:
    temp['nome'] = str(input('Fale um nome: '))
    temp['idade'] = str(input('Fale uma idade: '))
    controle = str(input('Deseja continuar? (s/n) '))
    print(temp)
    pessoas.append(temp.copy())
    print(pessoas)
    if controle == 'n':
        break