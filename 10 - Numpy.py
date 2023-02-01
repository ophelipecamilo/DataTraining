import numpy as np

# Criando uma matriz a partir de uma lista de valores

a = np.array([1,2,3])
print(a)

# Qtde de linhas e colunas
print(a.shape)

# Verificar dimensões
print(a.ndim)

# Criando matriz a partir de um range de valores
b = np.arange(1,10)
print(b)
print(b.ndim)

# Criando matriz a partir de valores espaçados linearmente

c = np.linspace(0,15, num=10)
print(c)
print(c.ndim)