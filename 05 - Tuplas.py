
# Tuplas = variáveis com mais de um valor

tuplas = ['Teste1', 'Teste2', 'Teste3']
print(tuplas)

tupla1 = ('Lanche','Batata','Refri')
tupla2 = (2, 6, 4, 5, 7)
tupla3 = (True, False , False)
tupla4 = ('Lanche',10.9, False, 2)

print(type(tupla4))
print(type(tupla4[0]))
print(type(tupla4[1]))
print(type(tupla4[2]))
print(type(tupla4[3]))
print()
print()

t1 = (0, 6, 4, 2, 8)
t2 = (1, 3, 3, 5, 3, 5, 7, 3)

len(t1)
print(len(t1))
sorted(t1)
print(sorted(t1))

t2.count(3)  # Contar quantas vezes o 3 aparece no t2
print(t2.count(3))

t2.index(7)  # Verificar o index do valor 7 aparece no t2
print(t2.index(7))

t2.index(3)  # Verificar o index do valor 3 aparece no t2
print(t2.index(3))

t2.index(3,4)  # Verificar o index do valor 3 aparece no t2 a partir da posição 4
print(t2.index(3,4))


# não é possível somar Tuplas... neste caso somente concatenar as duplcas

tt = t2 + t1
print(tt)