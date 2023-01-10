
# Listas são variáveis mutáveis declaradas em []

# Fatiamento [0]
# Métodos .index() .count()
# Funções len() sorted()
# Concaternar lista3 = lista 1 + lista2
# Lista dentro do for: for i in lista e for i,v in enumarate(lista):


# Modificando um valor

l1 = [2, 6, 4, 5, 7]
print(l1)

l1[2] = 3
print(l1)

# Alterando mais de um termo

l1[0:2] = [0,1]
print(l1)

# Adicionando termos

l1.append(8) # adicionando no final da lista
print(l1)

l1.insert(2, 2) # adicionando em posição específica
print(l1)

# Removendo/deletando termos de 3 formas

del l1[-1] #removi a última posição
print(l1)

var = l1.pop(-1)
print(l1)

l1.remove(5)
print(l1)

print()
print()

# Removendo vários valores em diversos argumentos da lista

l2 = [3, 2, 5, 0, 0, 8, 3, 8, 8, 4, 0, 9, 7, 8, 9, 3, 6, 0, 1]
print(l2)

qt = len(l2)
print(qt)

for i in l2:
    if 0 in l2:
        l2.remove(0)
print(l2)

qt2 = len(l2)
print(qt2)


# Ordenação de listar

l1 = [0, 3, 1, 7, 5, 7, 4]
print(l1)
print("Vamos ordernar!")
sort1 = sorted(l1)
print(sort1)

# Métodos não armazeam em variáveis, e sim organiza a variável original
sort2 = l1.sort()
print(sort2) 
print(l1)

# Listas em branco
lista = []
lista = list()

# Inserindo argumentos na lista

print(lista)

for i in range(1,6):
    lista.append(float(input('Digite o {}º número:'.format(i))))
print(sorted(lista))


# Declarando listas com o Range

eixox = list(range(0,100+1,1))

for i in eixox:
    # eixox[i] = eixox[i]/10
    eixox[i] /= 10
print(eixox)

print()
print()

l1 = [0,2,6,4,8,1,3]
print('Lista original: {}'.format(l1))

# Clonando listas

l2 = l1 # declaração igual permanece no mesmo espaço de memória

    # Deletando o último valor
l2.pop()

print('l1 = {}'.format(l1))
print('l2 = {}'.format(l2))

# Copiando listas

l2 = l1[:] # declaração com : cria um novo valor no espaço de memória

    # Deletando o último valor
l2.pop()

print('l1 = {}'.format(l1))
print('l2 = {}'.format(l2))


print()
print()

# Somando os argumentos de uma lista com o For --- Para listas com o mesmo tamanho

l1 = [0,2,6,4,8,1,3]
l2 = [3,2,1,7,8,2,5]
l3 = []

print('l1 = {}'.format(l1))
print('l2 = {}'.format(l2))

for i, val in enumerate(l1):
    print('Posição {} do l1, valor: {} e posição {} do l2, valor {}'.format(i,l1[i],i,l2[i]))
    l3.append(l1[i]+l2[i])
print('Lista 3: {}'.format(l3))


print()
print()


# Somando os argumentos de uma lista com o For --- Para listas tamanho diferente (considera o mesmo número de argumentos)

l1 = [0,2,6,4,8,1,3, 1, 5, 6]
l2 = [3,2,1,7,8,2,5, 2]
l3 = []

print('l1 = {}'.format(l1))
print('l2 = {}'.format(l2))

for v1, v2 in zip(l1,l2):
    print('l1 valor: {} e l2 valor {}'.format(v1,v2))
    l3.append(v1+v2)
print(l3)