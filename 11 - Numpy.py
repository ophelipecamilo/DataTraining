import numpy as np

a = np.arange(0,100)
print(a)
print(a.shape)
print(a.ndim)
print(a.size)

# Alterando o formato de uma Matriz.

b = a.reshape(10,10)
print(b)
print(b.ndim)
print(b.shape)
print(b.size)

# Converter a Matriz de 1 dimensão em 2 dimensões array

c = a[np.newaxis] # Linhas para colunas
print(c)
print(c.ndim)
print(c.shape)
print(c.size)


# Nova array

d = np.array([5,7,8,6,1,10,16,18,50,24,25,89,100,63,41,22,28,33,35,0])
print(d)

# Ordenando os elemntos

d2 = np.sort(d)

# Iterando com o array

for element in d2.flat:
    print(element)


# Concatenando

e = np.array([2,3,4,5,6])
f = np.array([7,8,9,10,11])

ef = np.concatenate([e,f])
print(ef)
print(ef.size)

# Juntando horizontalmente

ef2 = np.hstack((e,f))
print(ef2)
print(ef2.size)

# Juntando verticalmente

ef3 = np.vstack((e,f))
print(ef3)
print(ef3.size)

# Lista de arrays

ef4 = np.hsplit(ef, 5)
print(ef4)