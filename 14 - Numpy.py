import numpy as np
import matplotlib
import rasterio
from rasterio.plot import show

dataset = rasterio.open("C:/Temp/crop_rapideye.tif")

dataset_array = dataset.read(1) # Lendo valores binários da matriz

# Calculando média
media = dataset_array.mean()
print("Média = ", media)

# Desvio padrão
desv = dataset_array.std()
print("Desvio padrão: ", desv)

# Valor mínimo
mi = dataset_array.min()
print("Mínimo: ", mi)

# Valor máximo
ma = dataset_array.max()
print("Máximo: ", ma)

# Somar valores do array
soma = dataset_array.sum()
print("Soma: ", soma)

# Identificar valores únicos
unique_values = np.unique(dataset_array)
print("Valores unicos: ", unique_values)