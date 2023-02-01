import numpy as np
import matplotlib
# Lendo uma imagem de satélite
# Instalando biblioteca auxiliar para ler imagens
import rasterio
from rasterio.plot import show

dataset = rasterio.open("C:/Temp/crop_rapideye.tif")

dataset_array = dataset.read() # Lendo valores binários da matriz

# Verificar informações da matriz (imagem)

print("Elementos: ", dataset_array.shape) # número de elementos
print("Dimensões: ", dataset_array.ndim) # dimensões
print("Tipo de dado: ", dataset_array.dtype) # tipo de dado
print("Comprimento em bytes: ", dataset_array.itemsize) # comprimento em bytes
print("Tamanho total de elementos: ", dataset_array.size) # tamanho total