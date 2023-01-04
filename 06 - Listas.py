
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