import numpy as np

# Coeficientes de la matriz A
A = np.array([[3, 6], [-1, 2]])

comparacion = A % 2 == 0

# only even numbers
C = A[comparacion]

# Crear otro array para operaciones lógicas
array = np.array([1, 2, 3, 4, 5])
array_b = np.array([0, 1, 1, 0, 1])

# Operación lógica AND
resultado_and = np.logical_or(array > 2, array_b)


# Crear un array con un dato faltante
array_faltante = np.array([1, 2, np.nan, 4, 5])
print(f"array con datos faltantes: {array_faltante}")

print(np.mean(array_faltante))  # media de la columna

# Rellenar datos faltantes con la media del array
media = np.nanmean(array_faltante)  # Calcular la media ignorando los NaN
array_rellenado_media = np.where(np.isnan(array_faltante), media, array_faltante)

# open mtcars.csv

data = np.genfromtxt('data/mtcars.csv', delimiter=',', skip_header=1)

# print(data)
print(data.shape)  # Imprimir la primera fila

data_def = data[:, 1:]  # Eliminar la primera fila
print(data_def)  # Imprimir la primera fila