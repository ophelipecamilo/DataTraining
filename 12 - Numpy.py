import numpy as np

data = np.array([ [1,2],[3,4] ])
print("Data")
print(data)

print()
print("Ones")
ones = np.ones([2,2])
print(ones)

print()
somaArray = data + ones
print("Soma de Arrays - Data + Ones")
print(somaArray)

print()
subArray = data - ones
print("Subtração de Arrays - Data + Ones")
print(subArray)


# Outras operações

a = np.arange(1,16)
print("A")
print(a)
print()


zeros = np.zeros_like(a) # Criar com valores zerados
zeros + 2
print("Zeros + 2")
print(zeros)
print()


mult = a * zeros
print("Multiplicação")
print(mult)

div = a / zeros
print("Divisão")
print(div)